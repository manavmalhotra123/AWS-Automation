# AWS Inactivity Monitoring Tool

The AWS Inactivity Monitoring Tool is a Python script that helps you monitor and handle inactivity of your AWS resources, specifically EC2 instances and S3 buckets. It automatically stops idle EC2 instances and disables public access for inactive S3 buckets after a specified duration of inactivity.

## Features

- Monitors specified EC2 instances and S3 buckets for inactivity.
- Stops EC2 instances that have been idle for a defined threshold.
- Disables public access for S3 buckets that have been inactive for a specified duration.
- Customizable configuration to include/exclude resources and set the inactivity threshold.

## Prerequisites

Before running the tool, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- AWS IAM user credentials with the necessary permissions to interact with EC2 instances and S3 buckets.
- Boto3 library installed. Install using `pip install boto3`.

## Installation

1. Clone or download this repository to your local machine:


2. Install the required Python dependencies using the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

## Setup and Configuration

1. Modify `config.json`:

   - Open the `config.json` file in a text editor.
   - Add the EC2 instance IDs and S3 bucket names you want to monitor for inactivity to the respective lists.
   - Set the `inactivity_threshold_minutes` to the desired duration of inactivity before taking action (e.g., 10 minutes).

2. Add your AWS IAM user credentials to `main.py`:

   - Open `main.py` in a text editor.
   - Replace `"YOUR_ACCESS_KEY_ID"` and `"YOUR_SECRET_ACCESS_KEY"` with your actual AWS IAM user credentials.

3. Save the changes in `main.py` and `config.json`.

## How the AWS Inactivity Monitoring Tool Works

The AWS Inactivity Monitoring Tool continuously checks the specified EC2 instances and S3 buckets for inactivity. It calculates the time elapsed since the last activity for each resource and compares it with the `inactivity_threshold_minutes` value set in the `config.json` file.

- For EC2 instances:
  - If an EC2 instance has been inactive for longer than the specified threshold, the tool will stop that instance using the AWS EC2 API.

- For S3 buckets:
  - If an S3 bucket has been inactive for longer than the specified threshold, the tool will disable public access for that bucket using the AWS S3 API.

The tool provides real-time logs and notifications when taking actions on your AWS resources.

## Running the Tool as a Daemon (Linux/macOS)

To run the AWS Inactivity Monitoring Tool in the background as a daemon:

1. Ensure you have installed the `python-daemon` library:

   ```
   pip install python-daemon
   ```

2. Uncomment the line `with daemon.DaemonContext():` in `main.py`:

   ```python
   # Uncomment the line below if running on Windows or using python-daemon
   # with daemon.DaemonContext():
   main()
   ```

3. Save the changes in `main.py`.

4. Open a terminal, navigate to the project directory, and run the following command:

   ```
   python main.py
   ```

   The tool will now run as a background daemon, continuously monitoring the specified EC2 instances and S3 buckets for inactivity.

5. You can close the terminal without stopping the tool. The tool will keep running in the background.

## Running the Tool in a Separate Terminal

To run the AWS Inactivity Monitoring Tool in a separate terminal:

1. Open a terminal, navigate to the project directory, and ensure you are in the same virtual environment (optional but recommended).

2. Start the tool by running the following command:

   ```
   python main.py
   ```

   The tool will start monitoring the specified EC2 instances and S3 buckets for inactivity.

3. Leave the terminal open with the tool running while you work on your AWS tasks. The tool will keep running in the foreground, continuously monitoring your AWS resources for inactivity.

4. If you need to stop the tool at any point, go back to the terminal and press `Ctrl+C` to terminate the script.

## Important Note

- The tool performs actions (stopping EC2 instances and disabling S3 bucket public access) based on the inactivity threshold specified in `config.json`. Review and verify the configuration before running the tool in production to avoid unintended impacts on your AWS resources.

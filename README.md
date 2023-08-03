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
- (Optional for daemon mode) Python-daemon library installed. Install using `pip install python-daemon`.

## Setup and Configuration

1. Clone or download this repository to your local machine:

2. Modify `config.json`:

   - Open the `config.json` file in a text editor.
   - Add the EC2 instance IDs and S3 bucket names you want to monitor for inactivity to the respective lists.
   - Set the `inactivity_threshold_minutes` to the desired duration of inactivity before taking action (e.g., 10 minutes).

3. Add your AWS IAM user credentials to `main.py`:

   - Open `main.py` in a text editor.
   - Replace `"YOUR_ACCESS_KEY_ID"` and `"YOUR_SECRET_ACCESS_KEY"` with your actual AWS IAM user credentials.

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

## Important Note

- The tool performs actions (stopping EC2 instances and disabling S3 bucket public access) based on the inactivity threshold specified in `config.json`. Review and verify the configuration before running the tool in production to avoid unintended impacts on your AWS resources.



With these instructions, you can easily set up the AWS Inactivity Monitoring Tool and run it in the background as a daemon on Linux and macOS. Make sure to customize the `config.json` file with the resources you want to monitor, and add your AWS IAM user credentials to `main.py`.

Now, you can run the tool in the background and let it handle inactivity monitoring for your AWS resources while you work on other tasks.
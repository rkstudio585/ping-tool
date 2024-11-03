# Ping Tool

![Ping Tool Banner](https://via.placeholder.com/800x200.png?text=Ping+Tool) <!-- Placeholder for a banner image -->

## Overview

The **Ping Tool** is a simple yet powerful command-line utility built in Python that allows users to ping any website or IP address to check its availability and response time. The tool supports multiple pings with customizable timeout settings and logs the results for further analysis. Designed with user experience in mind, the tool features a professional and colorful interface using the `rich` library and ASCII banners with `pyfiglet`.

## Features

- **Ping Websites**: Check the availability of any website or IP address.
- **Custom Timeout**: Specify the timeout duration for each ping attempt.
- **Ping Statistics**: View statistics such as successful pings, average response time, and more after running the tool.
- **Log Results**: Automatically saves ping results to a log file for future reference.
- **User-Friendly Interface**: Utilizes `rich` for a visually appealing command-line interface.
- **Continuous Loop**: Allows users to continuously ping different websites without restarting the tool.
- **Easy Exit**: Gracefully exit the tool at any time by entering 'exit'.

## Installation

To install the Ping Tool, ensure you have Python 3.x installed on your system. You will also need to install the required libraries:

```bash
pip install rich pyfiglet
```

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/rkstudio585/ping-tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ping-tool
    ```

3. Run the tool:

    ```bash
    python ping.py
    ```

4. Follow the prompts to enter the website you wish to ping, the timeout duration, and the number of pings. Type `exit` to quit the tool at any time.

## Example Output

When you run the tool, it will look like this:

```planetext
Welcome to the Ping Tool
=========================
Trying to ping google.com (142.250.72.142)...
Ping to google.com successful! Time: 20.15 ms
Ping to google.com successful! Time: 21.10 ms
--- Ping statistics for google.com ---
Successful pings: 4/4
Average time: 20.63 ms
Log saved to google.com_ping_log.txt
```

## File Structure

```tree
ping-tool/
├── ping.py          # Main Python script for the Ping Tool
```

## Contributing

Contributions to the Ping Tool are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes. Ensure that your code is well-documented and adheres to the project style.

## Acknowledgements

- [Rich](https://rich.readthedocs.io/en/stable/) - For beautiful console output.
- [Pyfiglet](https://github.com/pwaller/pyfiglet) - For generating ASCII art.

## Contact

For questions or inquiries, feel free to reach out to me on GitHub: [rkstudio585](https://github.com/rkstudio585).

### Notes
- You can replace the placeholder link for the banner image with an actual image URL if desired.
- Feel free to modify any sections to better reflect your project's vision or any additional features you may want to highlight.

---

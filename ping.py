import socket
import time
import os
import threading
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from pyfiglet import figlet_format

# Initialize console for rich output
console = Console()

# Function to create an ASCII banner
def display_banner():
    banner = figlet_format("Ping Tool", font="slant")
    console.print(Panel(banner, title="Welcome to the Ping Tool", title_align="left", subtitle="Check the availability of websites", subtitle_align="right"), style="bold blue")

# Function to ping a website
def ping_website(hostname, timeout, count):
    ip = socket.gethostbyname(hostname)
    console.print(f"Trying to ping {hostname} ({ip})...", style="yellow")
    
    # Initialize statistics
    total_time = 0
    successful_pings = 0

    # Create log file
    log_file = f"{hostname}_ping_log.txt"
    with open(log_file, "w") as f:
        f.write(f"Ping log for {hostname}\n")
        f.write("Time(ms)\n")
    
    # Start pinging
    with Progress() as progress:
        task = progress.add_task("[cyan]Pinging...", total=count)
        
        for _ in range(count):
            start_time = time.time()
            try:
                # Attempt to connect to port 80
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(timeout)
                    result = s.connect_ex((ip, 80))
                    end_time = time.time()
                    
                if result == 0:
                    response_time = (end_time - start_time) * 1000  # Convert to milliseconds
                    total_time += response_time
                    successful_pings += 1
                    console.print(f"Ping to {hostname} successful! Time: {response_time:.2f} ms", style="green")
                    with open(log_file, "a") as f:
                        f.write(f"{response_time:.2f}\n")
                else:
                    console.print(f"Ping to {hostname} failed!", style="red")
            except socket.timeout:
                console.print(f"Ping to {hostname} timed out!", style="yellow")
            except Exception as e:
                console.print(f"An error occurred: {e}", style="red")
            finally:
                progress.update(task, advance=1)
                time.sleep(1)  # Wait for 1 second before the next ping

    # Display statistics
    if successful_pings > 0:
        average_time = total_time / successful_pings
        console.print(f"\n--- Ping statistics for {hostname} ---", style="bold")
        console.print(f"Successful pings: {successful_pings}/{count}")
        console.print(f"Average time: {average_time:.2f} ms", style="cyan")
        console.print(f"Log saved to {log_file}", style="green")
    else:
        console.print(f"No successful pings to {hostname}.", style="red")

# Main function to run the tool
if __name__ == "__main__":
    display_banner()
    
    while True:
        target = input("Enter the website to ping (e.g., google.com) or 'exit' to quit: ")
        if target.lower() == 'exit':
            console.print("Exiting the Ping Tool. Goodbye!", style="bold red")
            break
        
        try:
            timeout = input("Enter the timeout duration in seconds (default is 1): ")
            timeout = float(timeout) if timeout.strip() else 1.0
            count = int(input("Enter the number of pings to send (default is 4): ") or 4)

            # Run the pinging in a separate thread
            ping_thread = threading.Thread(target=ping_website, args=(target, timeout, count))
            ping_thread.start()
            ping_thread.join()  # Wait for the ping thread to finish

        except ValueError:
            console.print("Invalid input. Please enter numeric values for timeout and count.", style="bold red")
          

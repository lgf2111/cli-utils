# download_monitor.py

import os
import subprocess
import sys
import time


def check_file_exists(file_path):
    return os.path.exists(file_path)


def run_caffeinate():
    print("Running caffeinate...")
    caffeinate_process = subprocess.Popen(
        ["caffeinate", "-d"]
    )  # Run caffeinate in the background
    return caffeinate_process


def main(file_path):
    # Run caffeinate
    caffeinate_process = run_caffeinate()

    start_time = time.time()

    while check_file_exists(file_path):
        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Print a message indicating that the file is still downloading and the elapsed time
        print(
            f"File still downloading... Elapsed time: {elapsed_time:.2f} seconds",
            end="\r",
        )

        # Sleep for a short duration before checking again
        time.sleep(1)

    # File download complete, stop caffeinate
    caffeinate_process.terminate()

    # Print the total time taken
    end_time = time.time()
    total_time_taken = end_time - start_time
    print(
        f"\nFile download complete. Caffeinate stopped. Total time taken: {total_time_taken:.2f} seconds."
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_monitor.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

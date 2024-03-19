#!/usr/bin/env python

"""
MIT License

Copyright (c) 2024 InfoSecBD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import pyfiglet
import subprocess
import sys
import requests

# Developer: Md Mirajul Haque Miraj
# Engineer at InfoSecBD 

def generate_banner(tool_name):
    figlet = pyfiglet.Figlet()
    return figlet.renderText(tool_name)

def modify_wordlist(wordlist_file, interval, suffix):
    with open(wordlist_file, "r") as file:
        words = file.readlines()

    modified_words = []
    counter = 0

    for word in words:
        word = word.strip()
        modified_words.append(word)
        counter += 1
        if counter == interval:
            counter = 0
            modified_words.append(suffix)

    with open(wordlist_file, "w") as file:
        file.write("\n".join(modified_words))

def check_for_updates():
    try:
        response = requests.get("https://api.github.com/repos/MirajulHaque/isbdwordmod/releases/latest")
        if response.status_code == 200:
            latest_version = response.json()["tag_name"]
            return latest_version
    except Exception as e:
        print("Error:", e)
        return None

def perform_update():
    try:
        # Run a subprocess to execute a Git command to pull the latest changes
        subprocess.run(["git", "pull"])
    except Exception as e:
        print("Error:", e)

def main():
    tool_name = "isbdwordmod"
    version = "v1.0.0"

    banner = generate_banner(tool_name)

    print(banner)

    print(f"Version: {version}")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(prog="isbdwordmod", description="ISBD Wordlist Modifier Tool")
    parser.add_argument("-f", "--file", help="Wordlist file name with extension")
    parser.add_argument("-i", "--interval", type=int, help="Interval for adding the word")
    parser.add_argument("-s", "--suffix", help="String to be added after each interval")
    parser.add_argument("--update", action="store_true", help="Check for updates and perform update if available")
    args, _ = parser.parse_known_args()

    # Check if the user wants to perform an update
    if args.update:
        print("Checking for updates...")
        latest_version = check_for_updates()
        if latest_version and latest_version != version:
            print("Update available! Applying update...")
            perform_update()
            print("Update applied successfully.")
            sys.exit()
        elif latest_version:
            print("No updates available or already up-to-date.")
            sys.exit()
        else:
            print("Failed to check for updates. Continuing with the main functionality.")

    if args.update:
        return

    if args.file and args.interval and args.suffix:
        modify_wordlist(args.file, args.interval, args.suffix)
        print("Wordlist modified successfully!")
    else:
        print("Please provide the required arguments: -f/--file, -i/--interval, -s/--suffix")

if __name__ == "__main__":
    main()

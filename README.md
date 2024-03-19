# InfoSecBD Simple Wordlist Modifier Tool
The ISBD Wordlist Modifier Tool (isbdwordmod) is a command-line utility designed to modify wordlists by adding a specified string at regular intervals. This tool is useful for generating variations of wordlists for testing purposes, such as password cracking or dictionary attacks or brute-forcing.

## Features
- Add a specified string at regular intervals to a wordlist.
- Check for updates and perform updates if available.

## Installation
To install isbdwordmod, follow these steps:
1. Download the tool: Clone or download the isbdwordmod.py from the GitHub repository.
Link: https://github.com/MirajulHaque/isbdwordmod 
```bash
git clone https://github.com/MirajulHaque/isbdwordmod.git
```
2. Change Directory
```bash
cd isbdwordmod
```

3. Give Permission:

```bash 
chmod +x isbdwordmod.py
```

4. Move the script to a binary directory:
- To use isbdwordmod from any location in your terminal, you'll need to move the isbdwordmod.py to a directory included in your system's PATH environment variable.
- You can do this by executing the following command in your terminal:
```bash 
sudo mv isbdwordmod.py /usr/local/bin/isbdwordmod
```
This command moves the script to the /usr/local/bin/ directory, which is commonly included in the PATH variable. You may need to enter your password to authorize the move.

## Usage
1. Run the tool:
- Once the script is moved to a binary directory, you can use isbdwordmod from any location in your terminal. Open a terminal and run the following command:
```bash 
isbdwordmod --file <wordlist_file> --interval <interval> --suffix <suffix>
```

- Replace <wordlist_file> with the path to your wordlist file, <interval> with the interval for adding the string, and <suffix> with the string to be added after each interval.

- For example:
```bash
isbdwordmod --file wordlist.txt --interval 4 --suffix infosecbd
```
This command will modify the wordlist.txt file by adding the string "newword1" after every 4 words.

2. Check for updates: To check for updates and perform an update if available, run the following command:

```bash
isbdwordmod --update
```
This command will check for updates on the GitHub repository and update the tool if a new version is available.

## Developer
The ISBD Wordlist Modifier Tool is developed and maintained by Md Mirajul Haque Miraj. For any inquiries or feedback, please contact:

LinkedIn: [Md Mirajul Haque Miraj](https://www.linkedin.com/in/mdmirajulhaque/)
Facebook: [Md Mirajul Haque Miraj](https://www.facebook.com/MirajulHaqueOfficial.ME/)

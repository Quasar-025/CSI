## **grep**

This Python script simulates a grep-like command-line tool, allowing you to search for patterns in text files with various options and flags.

### **Features:**

- **Search:** Find lines containing a specified pattern in text files.
- **Flags:**
    - `c`: Case-sensitive search (default: case-insensitive)
    - `w`: Match whole words only
    - `n`: Count matches only
    - `i`: Invert match (find lines without the pattern)

- **Output:**
    - Highlights matched patterns in yellow.
    - Shows line numbers.
    - Displays the count of matches if `n` is used.

### **Usage:**

1. Run the script and you will be prompted with `:`
2. Start your command with grep then flags, pattern, location
    
    `python grep.py [-c] [-w] [-n] [-i] <pattern> <path>`
    
- Replace `<pattern>` with the text you want to search for.
- Replace `<path>` with the path to a file or directory.
- Use the flags as needed:
    - `c`: For case-sensitive search.
    - `w`: To match whole words only.
    - `n`: To count matches only.
    - `i`: To find lines without the pattern.

### **Example:**

 `:grep -i error log.txt`

This will search for lines that **don't** contain the word "error" in the file `log.txt`, ignoring case.
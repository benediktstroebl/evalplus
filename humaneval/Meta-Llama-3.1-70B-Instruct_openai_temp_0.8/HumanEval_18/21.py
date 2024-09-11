```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    if not string or not substring:
        # If either string or substring is empty, substring can't be found.
        return 0

    count = 0
    # Initialize a pointer to the start of the string.
    i = 0
    # Loop through the string until there's not enough characters left for substring.
    while i <= len(string) - len(substring):
        # Check if substring matches the current part of the string.
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the count.
            count += 1
        # Move the pointer one character to the right.
        i += 1

    return count

# Test cases
print(how_many_times('', 'a'))    # Expected output: 0
print(how_many_times('aaa', 'a')) # Expected output: 3
print(how_many_times('aaaa', 'aa')) # Expected output: 3
```
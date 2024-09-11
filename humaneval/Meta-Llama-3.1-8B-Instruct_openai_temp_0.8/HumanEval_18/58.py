```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the string.
    """
    count = 0
    string_length = len(string)
    substring_length = len(substring)
    
    for i in range(string_length):
        # Check if the substring can be found at the current position
        if string[i:i + substring_length] == substring:
            count += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script defines a function `how_many_times` that takes a string and a substring as input. It then iterates over the string, checking if the substring can be found at each position. If it can, it increments the count. The function finally returns the count. The test cases are included at the end of the script to verify that the function works as expected.
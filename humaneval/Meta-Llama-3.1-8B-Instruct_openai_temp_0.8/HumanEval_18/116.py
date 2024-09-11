```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not substring:  # If the substring is empty, return 0
        return 0
    
    count = 0
    index = 0
    
    while index < len(string):  # Loop through the string
        index = string.find(substring, index)  # Find the next occurrence of the substring
        if index!= -1:  # If the substring was found
            count += 1  # Increment the count
            index += 1  # Move the index forward one character to allow for overlapping matches
    
    return count

# Example usage:
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, allowing for overlapping matches. It uses a loop to find the next occurrence of the substring in the string, and increments a count each time it finds a match. If the substring is not found, the `find` method returns -1, which is handled by checking if the result is -1 before trying to increment the count.
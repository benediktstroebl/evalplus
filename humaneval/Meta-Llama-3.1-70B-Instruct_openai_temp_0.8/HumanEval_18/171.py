```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring is found in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    # Handle edge case where substring is empty
    if not substring:
        return 0

    # Initialize count of substring occurrences
    count = 0
    
    # Initialize index for searching
    i = 0
    
    # Search for substring in string, considering overlapping cases
    while i < len(string):
        # Check if substring is found at current index
        if string[i:i+len(substring)] == substring:
            # If found, increment count
            count += 1
        # Move index forward by 1
        i += 1
    
    # Return total count of substring occurrences
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

Alternatively, you can solve this problem using Python's built-in `str.find()` method in combination with a loop:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring is found in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    # Handle edge case where substring is empty
    if not substring:
        return 0

    # Initialize count of substring occurrences
    count = 0
    
    # Initialize index for searching
    i = 0
    
    # Search for substring in string, considering overlapping cases
    while i < len(string):
        # Find index of substring in string, starting from current index
        index = string.find(substring, i)
        
        # If substring is not found, exit loop
        if index == -1:
            break
        
        # If found, increment count
        count += 1
        
        # Move index forward by 1
        i = index + 1
    
    # Return total count of substring occurrences
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not substring:
        return 0
    
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Should print 0
print(how_many_times('aaa', 'a'))  # Should print 3
print(how_many_times('aaaa', 'aa'))  # Should print 3
```

Alternatively, you could use Python's built-in `str.find()` method in combination with a loop to achieve the same result:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not substring:
        return 0
    
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1
        else:
            break
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Should print 0
print(how_many_times('aaa', 'a'))  # Should print 3
print(how_many_times('aaaa', 'aa'))  # Should print 3
```
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    if not substring:  # If substring is empty, return 0
        return 0
    
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # Move start to the next character
        else:
            break
    return count


# Test cases
print(how_many_times('', 'a'))  # Should print 0
print(how_many_times('aaa', 'a'))  # Should print 3
print(how_many_times('aaaa', 'aa'))  # Should print 3
```

This Python script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string, counting overlapping cases. It then runs a few test cases to verify that the function works correctly.
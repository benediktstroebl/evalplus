Here's a Python function that solves the problem of finding the number of times a substring occurs in a given string. The function handles overlapping cases as described in the problem statement:
```python
def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.
    
    Args:
        string (str): Original string.
        substring (str): Substring to search for.
    
    Returns:
        int: Number of occurrences of the substring in the original string.
    """
    if not string or not substring:
        return 0
    
    counter = 0
    length = len(substring)
    n = len(string)
    
    for i in range(n - length + 1):
        if string[i:i+length] == substring:
            counter += 1
    
    return counter

# Tests
test_cases = [
    ('', 'a', 0),
    ('aaa', 'a', 3),
    ('aaaa', 'aa', 3),
    ('aaa', 'aaaa', 0),
    ('abababab', 'ab', 4)
]

for string, substring, expected in test_cases:
    result = how_many_times(string, substring)
    assert result == expected, f"For '{string}' and '{substring}', expected {expected} occurrences but got {result}"
```

The function works by initializing a counter to 0, then iterating through the length of the original string minus the length of the substring plus 1. This is done to account for the possibility of overlapping instances of the substring. Finally, the function returns the counter, which represents the number of times the substring occurs in the original string.
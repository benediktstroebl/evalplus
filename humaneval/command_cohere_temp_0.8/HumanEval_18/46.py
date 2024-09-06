Here's a Python function that solves the problem you've described, with the appropriate tests included:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    counter = 0
    substring_length = len(substring)
    string_length = len(string)
    
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            counter += 1
    
    return counter

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This code defines the `how_many_times` function, tests the edge cases, and verifies the function's behavior against the provided test cases.
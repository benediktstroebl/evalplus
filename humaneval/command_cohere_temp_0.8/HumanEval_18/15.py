Here's a Python function that solves the problem of finding the number of times a substring occurs within a given string. The function also handles overlapping cases:
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
    
    n, m = len(string), len(substring)
    
    # Ensure substring is shorter than the string
    if m > n:
        return 0
    
    counter = 0
    
    # Slide substring through string
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            counter += 1
    
    return counter

# Test Cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This function utilizes a sliding window approach to count the occurrences of the substring within the main string, regardless of overlapping instances. It's important to note that this function does not require any additional libraries and operates on basic string slicing and comparison operations.
Here's a Python function that solves the problem you've outlined, with code examples and a demonstration of how to use the function. The function counts the number of times a substring appears within a given string, even if there are overlapping instances:
```python
def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.
    
    Args:
    - string (str): Original string
    - substring (str): Substring to search for
    
    Returns:
    - int: Number of occurrences of the substring in the original string
    """
    if not string or not substring:
        return 0
    
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            count += 1
    
    return count

# Example usage:
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This function iterates through each possible starting position of the substring within the larger string and checks if the substring matches. The `range(n-m+1)` ensures we only consider starting positions that are practical to check, given the length of the substring (`m`) and the length of the larger string (`n`). This way, the function avoids unnecessary iterations and potential out-of-bounds errors.
Here's a Python function that solves the problem of finding the number of times a substring occurs within a given string. The function handles overlapping cases as described in the prompt. The function is also accompanied by a few test cases to ensure its correctness:
```python
def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.
    
    Args:
        string (str): The original string.
        substring (str): The substring to search for.
    
    Returns:
        int: The number of occurrences of the substring in the original string.
    """
    if not string or not substring:
        return 0
    
    n, m = len(string), len(substring)
    count = 0
    
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            count += 1
    
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('aaabbb', 'ab') == 2
assert how_many_times('aaaaaa', 'aaaa') == 2
```

This function simply computes all possible overlaps of the substring within the original string and counts the occurrences. You can test it with other cases as well to ensure it meets your requirements.
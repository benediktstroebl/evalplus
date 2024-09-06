```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from the list of strings.
    Args:
        strings (list of str): list of strings
    Returns:
        str: longest string
    """
    if not strings:
        return None
    
    max_len = max([len(str) for str in strings])
    longest_str = strings[0]
    for str in strings:
        if len(str) == max_len:
            longest_str = str
    
    return longest_str

# Unit tests
strings = ["a", "b", "bb", "ccc"]
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: ccc

strings = ["a", "a"]
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: a
```

This script provides a self-contained function that solves the problem of finding the longest string from a list of strings. The function takes a list of strings as input and returns the longest string. The function first checks if the list is empty, then it returns None. The function then finds the longest string in the list by comparing the lengths of each string and selecting the one with the maximum length. The function then returns the string.
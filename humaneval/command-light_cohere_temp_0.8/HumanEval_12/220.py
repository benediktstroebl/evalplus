Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    Args:
    strings (list of strings)
    Returns:
        str: longest string in the list
    """
    if not strings:
        return None
    return max(strings, key=len)

# Testing the function
strings = ["a", "b", "c"]
longest_result = longest(strings)
print(longest_result) # Output: c
```

In this code, the `longest()` function takes a list of strings as an argument and returns the longest string in that list. The function first checks if the list is empty, and if so, it returns None, as there is nothing to return. The function then uses the max() function with the `key=len` argument to return the string with the maximum length.
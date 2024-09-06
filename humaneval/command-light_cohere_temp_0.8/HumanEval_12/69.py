```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from a list of strings.
    Args:
        strings: list of strings
    Returns:
    str or None
    """
    if not strings:
        return None
    return max(strings, key=len)

# Unit tests
all_strings = ['a', 'b', 'bb', 'ccc', 'de']
longest_func = longest(all_strings)
print(longest_func)  # Output: 'ccc'
```
This code defines a Python function called longest that takes a list of strings as input and returns the longest string from that list. It uses the string length as the maximum operation and returns the result as a string. The function is then tested using the all_strings list, and the output is the longest string 'ccc' from the list.

This code demonstrates a clear separation of concerns and adheres to PEP 8 coding standards, making it readable and maintainable.
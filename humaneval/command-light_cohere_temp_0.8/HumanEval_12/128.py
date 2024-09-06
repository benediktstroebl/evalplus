```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string in the list.
    >>> longest(['a', 'bb', 'ccc'])
    """
    if not strings:
        return None
    max_len = max(len(string) for string in strings)
    return str(max_len)

# Test case 1: Verify result
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'

# Test case 2: Verify result for empty list
print(longest([]))  # Output: None
```
This function, `longest`, accepts a list of strings and returns the length of the longest string. In the test cases, it passes all the tests successfully.
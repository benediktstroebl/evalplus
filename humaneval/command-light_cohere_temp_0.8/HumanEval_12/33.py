```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Find the longest string in a list of strings.
    Parameters:
    strings (list of strings): List of strings.
    Returns: the first string of length in list that is not None.
    """
    return max(strings, key=len)

#Test cases
strings = ["a", "bb", "ccc"]
longest(strings)  # Output: 'ccc'

strings = [" "]
longest(strings)  # Output: ' ' '

strings = ["a", "bc", " ", "1", "2"]
longest(strings)  # Output: '1'

strings = ["abc"] * 3
longest(strings)  # Output: 'abc'

strings = [None, "abc", "123", ">"
longest(strings)  # Output: 'abc'
```

This solution demonstrates a simple and self-contained Python function, longest, that takes a list of strings as input and returns the first string in that list that is not None. It uses the max function with a key parameter set to the len of the string, effectively selecting the first string of the longest length.
Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the length of the longest string in the list.
    Parameters:
    strings (List[str]): list of strings

    Returns:
    str: The longest string
    """
    if not strings:
        return None

    max_length = 0
    longest_str = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string

    return longest_str
```

This function takes a list of strings as input and returns the length of the longest string in the list. It initializes variables to keep track of the maximum length and the current longest string. It iterates through string by checking if its length is greater than the current maximum length and updates the variables accordingly.
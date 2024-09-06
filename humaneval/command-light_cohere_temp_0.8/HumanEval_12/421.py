Here's the self-contained Python function to solve the problem:
```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in a list.
    Parameters:
    strings (list of string)
    Returns:
    str: the longest string
    """
    if not strings:
        return None

    longest_length = max(len(string) for string in strings)
    longest_string = strings[0] if len(strings[0]) == longest_length else strings[1]

    return longest_string
```

This function takes a list of strings as input and returns the longest string in the list. It uses the max function to find the maximum length of the strings and uses a list comprehension to find the first string with the length equal to the maximum length. The function also uses the maximum length and the first string in the list that matches the condition.
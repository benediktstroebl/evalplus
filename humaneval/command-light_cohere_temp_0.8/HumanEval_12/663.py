Here's a self-contained Python function that returns the longest string among a list of strings:
```python
def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    strings = [str for i in range(len(strings)):
        yield strings[i]
    strings = [x for x in strings if x!isalpha()]
    return max(strings, None)
```

This function takes a list of strings as input and returns the longest string. It iterates through each list of strings and returns the first occurrence of the longest string. The function is also designed to handle an empty list as input and return `None` in that case.
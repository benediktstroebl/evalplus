Here is a Python script that contains a self-contained function that correctly solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Input:
    list of strings
    Output:  string, or None if empty list
    """
    if not strings:
        return None
    return max(strings, key=len)
```
The code defines a function `longest` that takes a list of strings as input and returns the longest string in the list, or `None` if the list is empty. It uses the specific test time to maximize the string using the `len` function as the `key` argument of the `max` function, ensuring that the length of the string is used for comparison.
Here is a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: The length of the given string in Unicode code units.
    Args:
        string (str): The input string
        """
    if not string:  # Empty string
            return 0
    return len(string)
```
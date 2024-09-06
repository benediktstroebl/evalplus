```python
def count_distinct_characters(string: str) -> int:
    """
        Count the distinct characters in a given string, ignoring case.
        :return: The number of unique characters in the string
    """
    import string
    return len([char for char in string.isupper()])
```
This function utilizes the `str.isupper()` method to identify unique uppercase characters in the provided string, and then uses the `len()` function to count the resulting unique characters.
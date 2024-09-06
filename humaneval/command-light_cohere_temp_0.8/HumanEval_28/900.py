Here's a self-contained Python function that concatenates strings in a list into a single string:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)
```
This code provides a function that takes a list of strings as an input and returns the concatenated string.
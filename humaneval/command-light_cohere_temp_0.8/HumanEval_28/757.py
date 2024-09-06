Here's a self-contained Python function that solves the problem of concatenating strings:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string and return it.
    """

   :
        strings = ['a', 'b', 'c']
        return ''.join(strings)
    """
    return ''.join(strings)
```
This function takes a list of strings as an argument and uses the `join()` method to concatenate them into a single string, and then returns that string.
Here's the self-contained Python function:
```python
def concatenate(strings: List[str]) -> str:
    """
    Combine all given strings into a single string, return as markdown format.

    Args:
    strings (list of strings)
    """
    return ''.join(strings)
```
This function takes a list of strings as an argument and uses the join() method to concatenate the strings into a single string, which is then returned in markdown format.
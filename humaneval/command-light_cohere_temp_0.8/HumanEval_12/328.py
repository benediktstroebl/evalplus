Here's a self-contained Python function that takes a list of strings and returns the longest string.

```python
def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    list of strings = sorted(strings, key=len, reverse=True)
    return strings[-1]
```
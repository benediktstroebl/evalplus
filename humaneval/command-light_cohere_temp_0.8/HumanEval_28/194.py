Here's a self-contained Python function that receives a list of strings and returns the concatenated string:
```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
```

This function receives a list of strings and uses the `join` method to concatenate all strings in the list. When the list is empty, the function returns an empty string.
Certainly! Here's a self-contained Python function that takes a list of strings and returns their concatenation:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    """
    return ''.join(strings)
```

This function takes a list of strings as an argument and uses the `join` method to concatenate them into a single string. 
It then returns this concatenated string as the result.
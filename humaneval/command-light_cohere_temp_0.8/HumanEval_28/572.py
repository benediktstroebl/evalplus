Here's a self-contained Python function that concatenates strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
```

The function takes a list of strings as an argument and uses the `join` method to concatenate the strings into a single string.
Here's a self-contained Python function that finds the number of times a given substring can be found in the original string while avoiding overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """Count the number of occurrences of a substring in the string without case overlap."""
    return sum(1 for c in substring if c in string and c not in substring)
```
This function uses a generator expression with a lambda function to iterate over every character in the substring and checks if it's also in the original string. The 'sum' function then counts the number of times this happens to avoid case overlap.
```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

The function takes an input string and uses a list comprehension to generate a list of prefixes from the input string. The range of the iteration starts from 0 up to the length of the input string to include the full string itself as the longest prefix.
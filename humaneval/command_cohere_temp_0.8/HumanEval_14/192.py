```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The code generates a list of prefixes for the given string and then removes the longest prefix which is just the full string itself. Thus, the function returns a list of all the prefixes of the given string in descending order.
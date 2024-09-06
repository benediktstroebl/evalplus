```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The code leverages list comprehension to generate a list of prefixes for the given string and then removes the longest prefix which is simply the whole string itself.
```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The function constructs a list of prefixes of the given string and then removes the longest one which is simply the whole string itself. As a result, the list contains every prefix of the string from the shortest to the second longest.
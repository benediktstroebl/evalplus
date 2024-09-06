```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The code snippet above uses a list comprehension to generate a list of prefixes for the given string, starting from single characters and moving up to the full string itself. The '%' character is used as a placeholder to separate the prefixes. Finally, the list of prefixes is sliced to remove the last element ('%') and returned.
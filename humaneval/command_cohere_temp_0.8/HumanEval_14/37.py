```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This function defines a list of prefixes by using a list comprehension that generates all prefixes from the input string, ranging from the shortest (merely the first character) to the longest (the entire string).
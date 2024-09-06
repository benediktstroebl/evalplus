```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This function defines a list of prefixes, ranging from the smallest to the largest possible, based on the length of the input string. It uses a list comprehension to generate every possible prefix of the input string and returns it.
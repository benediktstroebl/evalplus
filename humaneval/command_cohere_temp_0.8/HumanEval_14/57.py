```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This script defines a function `all_prefixes` that takes a string as an input and returns a list of all prefixes of the string, from the shortest to the longest. The function uses a list comprehension to generate the prefixes, considering all possible prefixes of different lengths using `len(string) + 1` possible lengths. The resulting list of prefixes is ordered from shortest to longest since the generation process starts from an empty prefix and progressively adds characters to form longer prefixes.
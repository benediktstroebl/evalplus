```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the input string, ranging from the shortest to the longest. It employs a list comprehension to generate all possible prefixes of the input string by taking substring excerpts ranging from 0 to the length of the input string. The resulting list of prefixes is then returned. 

The `all_prefixes` function suffices as a self-contained solution for the problem statement, providing a straightforward way to obtain a list of prefixes for any given input string.
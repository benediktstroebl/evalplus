```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This script defines a function `all_prefixes` that takes a string as an input and returns a list of all prefixes of the string in length order from shortest to longest. It uses a list comprehension to generate the prefixes by taking substrings of the input string from the start up to each possible length of the input string.
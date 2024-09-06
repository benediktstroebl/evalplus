```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

The code defines a function `all_prefixes` that takes a string as an input and returns a list of all prefixes of the string in ascending order - from the shortest (the empty string) to the longest (the entire string).

The function uses a list comprehension to generate all possible prefixes of the input string. It iterates over the length of the string plus one (to include the empty string as the shortest prefix). For each length, it takes the corresponding number of leading characters from the input string as the prefix.

This code will produce a list of prefixes for any given input string, which serves the requirements of the provided problem statement.
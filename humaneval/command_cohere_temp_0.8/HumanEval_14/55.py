```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i == 0 else '') for i in range(len(string)+1)]
    return prefixes
```

This script defines a function `all_prefixes` that takes a string as an input and returns a list of all prefixes of the input string, from the shortest to the longest. The function uses a list comprehension to generate the prefixes by iterating through the length of the input string and combining the first i characters with an empty string if i is not 0, or with nothing if i is 0 (the shortest prefix).
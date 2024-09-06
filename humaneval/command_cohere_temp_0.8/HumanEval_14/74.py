```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i == 0 else ' ') * (len(string) - i) for i in range(len(string) + 1)]
    return prefixes
```

The function `all_prefixes` takes a string as input and returns a list of all prefixes of the string in order of decreasing length. The list of prefixes is generated using a list comprehension that iterates over the length of the string (from the length of the string to 1) and constructs each prefix using string slicing and some padding characters (' '), to make consecutive prefixes distinct.
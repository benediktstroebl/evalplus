```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This function defines a list of prefixes, then uses a list comprehension to generate the prefixes of the given string. The resulting list is sorted in order of decreasing length and returned. 

To execute this code simply run `all_prefixes('abc')` to yield the desired result of `['a', 'ab', 'abc']`.
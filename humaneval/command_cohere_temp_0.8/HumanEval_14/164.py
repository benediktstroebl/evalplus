```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

The function defines a list `prefixes` that stores all prefixes of the input string from the shortest to the longest. It uses a list comprehension that iterates over the length of the input string and slices the string from the beginning to that length to create all the prefixes. The list comprehension ranges from `i = 0` to `i = len(string)`, which effectively creates the list of prefixes from the shortest to the longest. The function returns the `prefixes` list. 

This approach ensures that the prefixes are sorted in ascending order of length and gives a list of all prefixes of the input string.
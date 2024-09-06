```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This function defines a list of all prefixes of the input string, ranging from the shortest (the empty string) to the longest (the entire string). This is achieved through list comprehension, which creates all possible prefixes of the string by taking slices of it from the start, considering all possible lengths (from 0 to n). 

Such a list of prefixes is then returned as the result.  This approach is efficient as it has a time complexity of O(n) due to the need to consider all possible prefixes, which results in an growing the prefixes list size proportional to the input size.
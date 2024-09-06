```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This function defines a list of all prefixes of the input string, ranging from the shortest (the empty string) to the longest (the entire string). 
The logic behind this code is that it uses a list comprehension to generate all possible prefixes of the input string by taking sub-strings starting from index 0 up to the length of the string.

The result is a list of prefixes sorted from the shortest to the longest, ready to be returned.
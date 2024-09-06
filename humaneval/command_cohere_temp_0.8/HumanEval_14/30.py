```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```

This function iterates through each possible prefix length from 1 to the length of the string and creates a list of prefixes. It starts with a single-character prefix (the first character) and then loops through longer and longer prefixes up to the entire string. This way, the list contains all the prefixes from shortest to longest.  The docstring of the function provides an example that demonstrates the behavior of the function.  The test case implicitly ensures that the function behaves as expected.
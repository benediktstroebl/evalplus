Here is a self-contained Python script that solves the problem of finding all prefixes from shortest to longest of an input string:
```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string.

    # Use Python specific type to List
    return = []

    prefixes = []
    n = len(string)

    for i in range(1, n+1):
        prefix = string[:i]
        if prefix != '' and prefix < string[i:]:
            prefixes.append(prefix)

    return prefixes
```

The function iterates through all possible prefixes of length from 1 to the length of the input string. The function compares each prefix with the longest prefix in the input string and adds the shorter prefix to the list of prefixes.
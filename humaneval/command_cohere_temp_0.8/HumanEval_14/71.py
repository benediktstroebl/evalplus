```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
The function `all_prefixes()` takes a string as input and returns a list of all prefixes in ascending order of length. It starts with a single character as the shortest prefix, then constructs longer prefixes by appending characters from the input string, and finally returns the sorted prefixes list.
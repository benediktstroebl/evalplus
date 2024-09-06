```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
The function all_prefixes creates a list prefixes, initially storing the first character of the input string. It then iterates through the remaining characters, appending to the prefixes list by using string slicing to create prefixes of increasing lengths until it reaches the full input string. The resulting list is returned, containing all the prefixes from the shortest to the longest.
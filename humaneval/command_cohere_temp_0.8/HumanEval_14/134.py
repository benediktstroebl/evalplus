```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
The function `all_prefixes` takes a string as input and returns a list of all prefixes in ascending order of length. It initializes the prefixes list with the single-character prefix at the start of the string. Then, it iterates through the string, appending each substring beforehand to the prefixes list, thereby creating all possible prefixes. The list of prefixes is returned once these iterations are completed.
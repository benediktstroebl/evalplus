```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(prefixes[-1] + string[i])
    return prefixes
```
The function all_prefixes creates a list prefixes, initially storing the first character of the input string. It then iterates through the remaining characters, appending the current character to the last prefix in the prefixes list, effectively creating a new prefix each time. This loop continues until all characters have been processed, leaving you with a list of prefixes from shortest to longest.
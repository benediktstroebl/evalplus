```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [str] * (len(string) + 1)
    prefixes[0] = ''
    for i in range(1, len(string) + 1):
        prefixes[i] = prefixes[i - 1] + string[i - 1]
    return prefixes
```
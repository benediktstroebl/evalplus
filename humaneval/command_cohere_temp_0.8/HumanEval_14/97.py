```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(prefixes[-1] + string[i])
    return prefixes
```
This code uses a list to store the prefixes of the given string, starting with the single-character prefix when the string length is 1, and gradually constructing longer prefixes by appending the next character at each iteration until it reaches the original string as the longest prefix.
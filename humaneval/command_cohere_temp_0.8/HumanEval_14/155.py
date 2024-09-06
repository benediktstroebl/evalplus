```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
The function all_prefixes creates a list prefixes, which initially stores the single-character prefix of the input string, namely the first character of the string. Subsequently, it iterates from the second character onwards, appending each prefix created by taking characters from the start of the string up to the current position to the prefixes list. This process continues until the end of the string is reached. As a result, the list prefixes is populated with all the prefixes of the input string, ranging from the shortest, which is a single character, to the longest, which is the entire string.
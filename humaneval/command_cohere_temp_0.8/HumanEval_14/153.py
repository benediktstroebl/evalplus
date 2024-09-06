```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [str]
    for i in range(1, len(string)+1):
        substr = string[:i]
        prefixes.append(substr)
    return prefixes
```
The function `all_prefixes()` takes a string as input and returns a list of all prefixes of the input string, from the shortest to the longest. This is achieved by iteratively appending substrings of the input string to a list, with the substrings ranging in length from 1 (the input string itself) to the length of the input string. The result is a list of prefixes in the desired order.
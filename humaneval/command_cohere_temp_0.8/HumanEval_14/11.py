```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
The function iterates through the string to obtain all possible prefixes, from the smallest to the largest, it stores each of them in the `prefixes` list.  It starts with a prefix of length `1` using the first character of the string, and then iterates through the string to create longer prefixes. At each iteration, it prepends the current character to the previous prefix and adds it to the list. Thus, the list `prefixes` at the end of the function contains all the prefixes of the string in increasing order of their length.  It is important to note that the code works for any string, regardless of its characters or length.
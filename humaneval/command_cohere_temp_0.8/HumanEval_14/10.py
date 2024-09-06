```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(prefixes[-1] + string[i])
    return prefixes
```
The `all_prefixes` function starts with an empty list, prefixes, and systematically adds substrings of the input `string` to it. It does this by starting with the shortest substring, which is the first character of the string (converted to a string itself), and then iteratively adding the next character to the previous prefix until it reaches the full string's length. This way, the list contains all prefixes in ascending order.
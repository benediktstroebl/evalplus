```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```

This function iterates through the string character by character and appends to the `prefixes` list differently based on the index of character:
- The first character is added as a single element at the beginning of the list.
- For each subsequent character, the function prepends the string up to that point to the list, thus creating a new prefix.

The list is then ordered from the shortest (first element) to the longest (last element) prefix.
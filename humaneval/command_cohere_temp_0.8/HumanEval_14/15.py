```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The code generates a list of prefixes for the given string and then removes the longest prefix which is simply the whole string prefixed with '%' (to ensure uniqueness). The resulting list is ordered from shortest to longest prefix. 

The idea is to use list comprehension to generate a list of prefixes of `string` from length 1 to `length(string)` with a special prefix character '%' added to the end of each prefix to ensure uniqueness, and then remove the longest prefix which is the whole string itself.
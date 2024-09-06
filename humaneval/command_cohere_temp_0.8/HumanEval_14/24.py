```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The function constructs a list where each element represents a prefix of the input string, with the shortest prefix being '%' (which is also an empty string). It does this by using a list comprehension that iterates through the length of the string and constructs each prefix accordingly. The final list excludes the longest prefix which is just the string itself, resulting in a list of all prefixes from shortest to longest.
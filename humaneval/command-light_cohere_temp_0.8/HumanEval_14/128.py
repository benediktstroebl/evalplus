Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of the input string:
```python
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string]
```

This function employs list comprehension to iterate through each character in the input string and creates a new string by prepending each character. The resulting list of prefixes is then returned.
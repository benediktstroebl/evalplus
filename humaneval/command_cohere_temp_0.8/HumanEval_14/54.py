```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i==0 else '') for i in range(len(string)+1)]
    return prefixes
```

The function uses a list comprehension with a range starting from 0 to `len(string)+1` to create a list of prefixes of the input string. It prepends single characters to the empty string to create the prefixes, which include the input string itself, its single prefixes, as well as the empty string. The list is sorted to ensure that the output is always `[empty, character, two_characters, ... input_string]`.
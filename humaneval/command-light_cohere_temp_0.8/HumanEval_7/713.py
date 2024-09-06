Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for those that contain a given substring:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.lower() == substring.lower()]

```

>>> test_filter_by_substring([anything(), 'asdf'])
 ['asdf']
>>> test_filter_by_substring(['hello', 'world', '!add', 'as'])
['hello', 'world']
```

This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. The function uses a `includes.lower()` to ensure that the strings are all lowercase before checking if the substring is present, which is the intended behavior.
Here's the self-contained Python function that solves the problem of finding all prefixes from the shortest to longest of any input string:
```python
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.group(string) if prefix not in string.group('')]

# tests
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```
This function employs the set comprehension technique to generate a list of all prefixes in the input string. By utilizing the string.group and the group(string), the function creates a set of all prefixes and removes any duplicates, ensuring an array with distinct prefixes.
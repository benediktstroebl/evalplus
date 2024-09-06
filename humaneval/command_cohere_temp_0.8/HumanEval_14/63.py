```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```

This function iterates through the input string and constructs a list of prefixes, ranging from the shortest (the first character) to the longest (the full string). It does so by adding individual characters and full substrings to the `prefixes` list.

Here's how you can call this function with the test case provided:
```python
test_string = 'abc'
expected_prefixes = ['a', 'ab', 'abc']

assert all_prefixes(test_string) == expected_prefixes
```
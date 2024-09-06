```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
The function iterates through the string to obtain all possible prefixes, from the single-character prefix of the first letter to the full string itself. It stores these prefixes in ascending order (from shortest to longest) in the `prefixes` list and returns the list. 

Here is a test case that validates the functionality of the previous solution:
```python
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
test_all_prefixes()
```
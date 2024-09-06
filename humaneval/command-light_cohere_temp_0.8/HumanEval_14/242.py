Here is a Python script with a self-contained function that solves the problem of finding all prefixes from shortest to longest of a given string:
```python
import typing
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ["".join([char for c in string if c <= ord(i) < ord('z') else i for i,char in enumerate()])
```
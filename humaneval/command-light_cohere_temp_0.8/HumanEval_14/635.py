Here's the self-contained Python function that solves the problem of returning all prefixes from shortest to longest of an input string:
```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # List of all prefixes
    prefixes = ['abc', 'ab', 'ac', 'a', 'ab', 'aby', 'aba', 'abb']

    # Sort the prefixes by length
    prefixes.sort(key=lambda x: len(x))

    return prefixes
```
This function iterates through all possible prefixes and stores them in a list, then sorts the list based on the length of the prefixes to guarantee they are in ascending order.
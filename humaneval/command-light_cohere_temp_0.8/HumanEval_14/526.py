```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return ['']

    # UseTailoring returns the most specific function from a
    # function family based on the arguments passed
    return list(UseTailoring('lp', string, (0, 0)))

def UseTailoring(func_family: str, string: str, arg: Tuple[int, int]) -> List[str]:
    """ Helper function to return the most specific function from a function family.
    >>> Use function family is using the arguments to the registered function."""
    if func_family == 'lp':
        # Using Levenshtein as the default function for string preprocessing
        # We want the shortest function, so we return the function with
        # the smallest arg[0]
        return [f(string, arg) for f in functions[func_family]]

    return []

# Dictionary with registered functions for Levenshtein
functions = {
    'lp': [lambda s, i: s[i] if i < len(s) else 0],
             lambda s, j: s[j] if j < len(s) else 0]
}
``` 
Note that the solution assumes the input is a string containing only ASCII characters.
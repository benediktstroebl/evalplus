```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function splits the string of nested parentheses into a list of its deepest nesting levels.
    Returns a
    list of deepest nesting levels.
    """

    list comprehension is a bit.
    """ This recursive string matching.

    >>> test_parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    pattern = r'\((\))+'
    return [len(x) for x in re.findall(pattern, parent_string)]
```
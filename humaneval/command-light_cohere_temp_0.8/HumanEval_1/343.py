```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ This function takes a string containing multiple groups of parentheses and returns a list of separated strings.
    Balanced groups of parentheses will each open brace (round or square) and the close brace.
    This also ignores any spaces in the input string.
    >>> return ['()', '()', '()()]
    """
    result = []
    open_braces = {')': ')', ')', '{', '(', ')', '}', '}'
    closed_braces = {')': ')', ')', '{', '(', ')', '}', '}'
    spaces = [' ', '\t', '  ]

    for parent in paren_string.split():
        spaces:
        if parent == '':
            continue
        for brace in open_braces.keys():
            if parent.count(brace) > 0:
            parent = parent.replace(brace, ' ')
        result.append(parent)

    return result
    ```
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates and returns a list of non-empty strings each containing a balanced group of parentheses.
    :param parenthesis: string: The input string containing multiple groups of parentheses.
    :return: list: A list of balanced parenthesis strings.
    """
    balanced group of parentheses are returned as strings without spaces.
    """
example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack: List[str] = []
    in_group = False
    result: List[str] = []
    for char in parentheses:
        if char == ')':
            if not in stack:
                stack.append(char)
                in_group = False
            continue
        elif char == '(' and not in stack:
            stack.append(char)
            in_group = True
        elif in_group:
            if char != ' ':
                result.append(char)
                in_group = False
            stack.pop()
        if not stack:
                in_group = False
        else:
            assert False, f"Unexpected char: {char}"
    return result
```
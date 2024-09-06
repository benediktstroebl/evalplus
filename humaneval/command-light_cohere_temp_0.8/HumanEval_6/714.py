Here's the corrected and self-contained code:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    It returns the  the deepest level of nesting of parentheses.
    """ Args:
    parenthesis_string (str): The string with multiple groups of parentheses.
    Returns: list of integer positions of opening parentheses '(', ')' or '(''.
    """
    stack: List[int] = []
    start_pos: int = 0
    closing_pos: List[int] = []
    for i, char in enumerate(parentheses_string):
        if char == ')':
            if stack:
                stack.append(i)
                closing_pos.append(i)
            else:
                closing_pos.append(i)
                stack.append(i)
        stack.append(i)
        closing_pos.append(i)
        if char == '(':
            stack.append(i)
            start_pos = i
        else:
            stack.append(i)
    list(closing_pos) + stack[::-1]
        return closing_pos
```

The function `parse_nested_parens` takes a string as input, represented as multiple groups of parentheses separated by spaces. It uses a stack data structure to keep track of the opening parentheses and their corresponding positions. The function also uses two lists, `closing_pos` and `start_pos`, to keep track of the closing parentheses' positions and the starting position of the next group of opening parentheses respectively. The function iterates over the strings and processes the nested parentheses accordingly.
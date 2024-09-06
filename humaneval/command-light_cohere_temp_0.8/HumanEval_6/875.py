```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes in a string of nested parentheses and returns a list of the deepest level parentheses found.
    Test cases have also been provided to make sure the function works as expected.
    """

    test cases:
    - '(()()) ((())) () ((()))' -> [2, 3, 1, 3]
    - '(((((()))))))' -> [4, 3, 2]
    - '(((((())))))())' -> [4, 3, 2]
    - '(((((())))))())()' -> [4, 3, 2]
    - '(())()()' -> []
    - '(()())' -> []
    - '()()()()' -> []
    """
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                stack.append('(')
            else:
                stack.append(')')
    stack.append(char)
    for char in stack:
                if char == '(':
                    stack.append('(')
                else:
                    if len(stack) == 0:
                        stack.append(')')
                else:
                    stack.append(' ')

    return stack
```
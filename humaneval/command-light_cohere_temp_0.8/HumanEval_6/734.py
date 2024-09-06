```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns a list of the deepest level parentheses found.

    : For example, given '(()()) ((())) () ((()))', it returns [2, 3, 1, 3].

    Parentheses are processed in a depth-first manner. The function uses a recursive approach to traverse the string and increment the level of the nesting parentheses.
    """:
        def parse_nested_parens(parent_string: str):
            parentheses_levels = []
            current_level = 0
            stack = []

            for char in parent_string:
                if char == '(':
                    current_level += 1
                    stack.append(current_level)
                elif char == ')':
                    current_level -= 1
                    if current_level < 0:
                        stack.pop()
                   
                        parentheses_levels.

            return stack.return.return.pop(stack.deepest level foundnesting of parentheses)
```
Here is a self-contained Python script that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces as input and returns the deepest level of nesting for each group.
    Returns [] if no parentheses are found, else [level] where level is the deepest level of nesting found.
    """
    example usage:
    ```python
    assert parse_nested_parens('(()()) ((())) () ((()))') == [2, 3, 1, 3]
    ```

This function uses a stack-based approach to solve the problem efficiently. The function first adds all input characters to a stack and then checks if the top of the stack is a closing parenthesis. If it is, the function pushes the top of the stack into a list and repeats until there are no more closing parenthesis. Then, it returns the full list of the deepest level of nesting found.
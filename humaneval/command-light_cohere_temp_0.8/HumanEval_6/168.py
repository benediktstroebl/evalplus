```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input and returns a list of the deepest levels of nesting.
    Input:
    - The function accepts a string parent_string, which is a representation of multiple groups of parentheses separated by spaces.
   
    - The function returns a list of the deepest levels of nesting in the parentheses.
    - It example input is '(()()) ((())) () ((()))()())'
    - This would return [2, 3, 1, 3]
    - The function uses a depth-first traversal to find the correct nesting levels.
    """
   
    tests. The function tests a passed against the tests that verify the correct behavior of the function.
```
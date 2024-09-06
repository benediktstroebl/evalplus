```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function tries to parse and return the deepest level of nesting of parentheses from the input string.

    Args:
        string parent_string: str containing multiple groups of parentheses separated by spaces.

    Returns:
    list of integers in the order of increasing nesting level, or an error if not enough levels are provided.
    """
    test:
        Test case with correct input.
    """ Input should be a example with multiple groups of parentheses, separated by spaces.

Example:
```python
parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This function uses a recursive approach with a stack to keep track of the current level of nesting.  It returns a string with integers representing the nesting level of each parent.
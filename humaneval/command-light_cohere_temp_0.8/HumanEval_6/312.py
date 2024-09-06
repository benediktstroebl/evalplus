```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input and returns a list of deepest level parentheses found.
    """

    function uses recursive backtracking to traverse the string and returns the level of each parent from deepest to shallowest.
    """

    code uses the time complexity of O(n), where n is the length of the string, due to the recursive nature of the algorithm.
    Args:
        parent_string (str): The string to parse with nested parentheses
    Returns:
    List[int]: A list of deepest level parentheses found, starting from deepest to shallowest
    """
    stack: List[int] = []
    parent_level: int = 0
    result: List[int] = []
    for char in parent_string:
        if char == "(" and parent_level > 0:
            stack.append(parent_level)
            parent_level += 1
        elif char == ")" and parent_level > 0:
            parent_level -= 1
        elif parent_level == 0:
            result.append(stack.pop())
   
            deepest level of parentheses is the stack.
# Test cases
```
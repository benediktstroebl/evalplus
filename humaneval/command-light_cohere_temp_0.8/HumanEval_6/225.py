```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    Parses a string of multiple groups of nested parentheses separated by spaces and returns the deepest level of nesting.
    Input: String of parentheses separated by spaces.
    Return: List of index locations of each group of parentheses.
    """ Requires spaces to separate groups.
    """ Assumes format of a string where the first and last parentheses match the deepest level of nesting.

# Test Case 1:
Input: ((()))()((()()))()
Expected Output: [2, 3, 1, 3]
# Test Case 2:
Input: ((()()))
Expected Output: []
# Test Case 3:
Input: (())()()
Expected Output: []
# Test Case 4:
Input: (())
Expected Output: []
```
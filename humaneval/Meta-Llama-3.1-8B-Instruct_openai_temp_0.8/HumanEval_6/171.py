### Parse Nested Parentheses
#### Problem Statement:
Given a string of nested parentheses separated by spaces, parse each group and return the deepest level of nesting.

#### Solution:
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of nested parentheses and return the deepest level of nesting for each group.

    Args:
    paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    groups = paren_string.split()

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        result.append(max_depth)

    return result
```
#### Explanation:
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of integers representing the deepest level of nesting for each group.

Here's a step-by-step breakdown:

1. Split the input string into groups using the `split` method.
2. Iterate through each group.
3. Initialize `max_depth` to 0 and `current_depth` to 0.
4. Iterate through each character in the group.
   * If the character is an opening parenthesis `(`, increment `current_depth` and update `max_depth` if necessary.
   * If the character is a closing parenthesis `)`, decrement `current_depth`.
5. Append `max_depth` to the `result` list after processing each group.
6. Return the `result` list.

You can test the script using the provided example input: `parse_nested_parens('(()()) ((())) () ((())()())')`.
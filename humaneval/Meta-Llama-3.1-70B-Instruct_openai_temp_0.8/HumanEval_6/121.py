```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string containing multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """

    def calculate_depth(group: str) -> int:
        """
        This helper function calculates the deepest level of nesting for a given group of parentheses.

        :param group: A string containing a group of nested parentheses.
        :return: An integer representing the deepest level of nesting for the group.
        """
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()

    # Calculate the deepest level of nesting for each group
    depths = [calculate_depth(group) for group in groups]

    return depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers, where each integer represents the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces
    :return: A list of integers representing the deepest level of nesting for each group
    """

    def deepest_nesting(paren_group: str) -> int:
        """
        This helper function calculates the deepest level of nesting for a single group of parentheses.

        :param paren_group: A string representing a single group of nested parentheses
        :return: The deepest level of nesting for the group
        """
        max_depth = 0
        current_depth = 0
        for char in paren_group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()

    # Calculate the deepest level of nesting for each group and return the results as a list
    return [deepest_nesting(group) for group in paren_groups]


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
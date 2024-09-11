```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """
    def max_nesting_depth(group: str) -> int:
        """
        This helper function calculates the maximum nesting depth for a single group of parentheses.

        :param group: A string of nested parentheses.
        :return: The maximum nesting depth.
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

    # Calculate the maximum nesting depth for each group
    return [max_nesting_depth(group) for group in groups]


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
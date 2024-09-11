```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list where each element is the deepest level of nesting of the corresponding group.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of the deepest level of nesting for each group.
    """
    def max_depth(paren_group: str) -> int:
        """
        Helper function to calculate the deepest level of nesting for a single group.
        It uses a stack to track the opening and closing of parentheses.

        :param paren_group: A string of nested parentheses.
        :return: The deepest level of nesting.
        """
        stack = 0
        max_stack = 0
        for paren in paren_group:
            if paren == '(':
                stack += 1
                max_stack = max(max_stack, stack)
            elif paren == ')':
                stack -= 1
        return max_stack

    # Split the input string into groups and calculate the max depth for each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the deepest level of nesting for each group using a helper function `max_depth`. The `max_depth` function uses a stack to track the opening and closing of parentheses in a single group. The script then tests the function with the provided example.
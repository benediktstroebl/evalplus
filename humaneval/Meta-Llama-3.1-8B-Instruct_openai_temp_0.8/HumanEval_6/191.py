```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces.
    It returns a list where each element is the maximum level of nesting for the corresponding group.

    :param paren_string: A string of groups of nested parentheses separated by spaces.
    :return: A list of integers representing the maximum level of nesting for each group.
    """
    def max_depth(group: str) -> int:
        """
        This helper function calculates the maximum depth of nesting for a single group.
        It uses a stack to keep track of the opening parentheses and returns the maximum depth.

        :param group: A string representing a group of nested parentheses.
        :return: The maximum depth of nesting for the group.
        """
        stack = 0
        depth = 0
        for char in group:
            if char == '(':
                stack += 1
                depth = max(depth, stack)
            elif char == ')':
                stack -= 1
                depth = max(depth, stack)
        return depth

    groups = paren_string.split()
    return [max_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, the `parse_nested_parens` function splits the input string into groups and then uses a helper function `max_depth` to calculate the maximum depth for each group. The `max_depth` function uses a stack to keep track of the opening parentheses and returns the maximum depth. The result is a list of integers representing the maximum level of nesting for each group.
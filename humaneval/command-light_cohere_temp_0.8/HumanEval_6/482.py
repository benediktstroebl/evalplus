```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses and returns the counts of each level of nesting.
    """
    expected format is a string with multiple groups of parentheses separated by spaces.
    """
    groups of parentheses can have any nesting level, with the maximum level being 3.

    Returns: list of counts of each level of nesting.
    """ For nested parentheses must be in any order.
    """
    an empty string "" returns []
    """
    def parse_parentheses(parent_string: str) -> List[int]:
        stack = []
        result = []

        for char in parent_string:
            if char == "(":
                stack.append(1)
            elif char == ")":
                if stack:
                    level = stack.pop()
                    max_level = len(stack)
                    result.append(max_level)
                stack.append(0)
            elif char == "(" and stack:
                stack.append(1)
            elif char == ")": and stack:
                stack.pop()
        result.append(0)
            return result
        return result
    return result

# Test
test_str = "((())) ((())) () ((()))"
test_result = parse_parentheses(test_str)
print(test_result)
``` 
This script defines a function `parse_parentheses` that takes a string of nested parentheses and returns a list of counts of each level of nesting. The test string provided is `"((())) ((())) () ((()))"`, which is passed to the `parse_parentheses` function and the corresponding result is printed.
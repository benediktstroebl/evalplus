```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses in each group of a given string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers where each integer is the deepest level of nesting of parentheses in the corresponding group.
    """
    result = []
    groups = paren_string.split()

    for group in groups:
        count = 0  # Initialize the count of open parentheses
        max_count = 0  # Initialize the maximum count of open parentheses
        for char in group:
            if char == '(':
                count += 1
                max_count = max(max_count, count)
            elif char == ')':
                count -= 1
                assert count >= 0  # If count becomes negative, it means there's an extra closing parenthesis
        result.append(max_count)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that splits the input string into individual groups of nested parentheses, calculates the maximum nesting level for each group, and returns the results as a list of integers. The function uses a counter to track the current level of nesting and updates the maximum level as needed. The script also includes a unit test to verify the correctness of the function.
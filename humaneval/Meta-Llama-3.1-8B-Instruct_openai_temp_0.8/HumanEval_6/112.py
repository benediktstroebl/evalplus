```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest levels of nesting for each group of parentheses.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()

    results = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a stack to track the deepest level of nesting
        stack = []
        
        # Initialize the deepest level of nesting for this group
        deepest_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()
                    # If the stack is empty after popping, this is the deepest level of nesting for this group
                    if not stack:
                        deepest_level = max(deepest_level, len(stack) + 1)
        
        # Append the deepest level of nesting for this group to the results list
        results.append(deepest_level)

    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input and returns a list of the deepest levels of nesting for each group. The function uses a stack to track the deepest level of nesting for each group and iterates over each group of parentheses to calculate the deepest level of nesting.
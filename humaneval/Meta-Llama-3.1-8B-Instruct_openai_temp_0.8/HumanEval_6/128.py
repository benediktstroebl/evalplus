### Nested Parentheses Depth Calculator
#### Problem Description

The following Python script calculates the deepest level of nesting of parentheses in multiple groups separated by spaces.

#### Code
```python
from typing import List


def calculate_depth(s: str) -> int:
    """
    Calculate the deepest level of nesting of parentheses in a string.
    
    :param s: Input string containing nested parentheses.
    :return: The deepest level of nesting of parentheses.
    """
    depth = 0
    max_depth = 0
    for char in s:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            if depth > 0:
                depth -= 1
    return max_depth


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Calculate the deepest level of nesting of parentheses for multiple groups separated by spaces.
    
    :param paren_string: Input string containing multiple groups of nested parentheses separated by spaces.
    :return: A list of deepest levels of nesting of parentheses for each group.
    """
    groups = paren_string.split()
    return [calculate_depth(group) for group in groups]


# Example usage
if __name__ == "__main__":
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Explanation

The `calculate_depth` function iterates through the input string and keeps track of the current depth of nesting. Whenever it encounters a '(', it increments the depth; whenever it encounters a ')', it decrements the depth if the depth is greater than 0 (to avoid considering unmatched '(' as part of the nesting depth).

The `parse_nested_parens` function splits the input string into groups separated by spaces and applies the `calculate_depth` function to each group.

The script includes an example usage at the end to demonstrate its functionality.
### Python Script to Parse Nested Parentheses
```markdown
### Code
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    output = []
    for group in paren_string.split():
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        output.append(max_depth)
    return output

### Test the function
if __name__ == "__main__":
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

### Explanation
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. The function iterates over each group of parentheses in the input string, and for each group, it keeps track of the current depth and the maximum depth encountered so far. When it encounters a closing parenthesis, it subtracts 1 from the current depth. Finally, it appends the maximum depth for each group to the output list and returns the list.

The script includes a test case to demonstrate the function's behavior. When you run this script, it will output `[2, 3, 1, 3]`, which is the correct result for the input string `'(()()) ((())) () ((())()())'`.
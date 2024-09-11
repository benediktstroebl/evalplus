```markdown
### Parsing Nested Parentheses
#### Problem Description

Given a string of nested parentheses groups separated by spaces, 
output the deepest level of nesting for each group.

#### Solution

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of nested parentheses groups separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        stack = []
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                stack.pop()
                if not stack:
                    depth = 0
        result.append(max_depth)
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Explanation

1.  The function `parse_nested_parens` takes a string of nested parentheses groups as input.
2.  It splits the input string into individual groups using the `split` method.
3.  For each group, it initializes a stack to keep track of the opening parentheses and a variable `depth` to keep track of the current nesting level.
4.  It iterates through each character in the group. If it encounters an opening parenthesis, it pushes it onto the stack and increments the `depth`. If it encounters a closing parenthesis, it pops the stack and resets the `depth` to 0 if the stack is empty.
5.  The `max_depth` variable keeps track of the maximum nesting level encountered so far.
6.  After processing each group, it appends the maximum nesting level to the result list.
7.  Finally, it returns the result list containing the maximum nesting levels for each group.
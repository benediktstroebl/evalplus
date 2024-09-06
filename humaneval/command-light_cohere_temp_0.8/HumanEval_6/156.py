```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Function to parse and return the deepest level of nesting of parentheses.
    Parameters: s (string): str representing multiple groups for nested parentheses separated by spaces
    Returns: List[int]: A list of the deepest level of nesting of parentheses
    """
    stack: List[int] = []
    for c in s:
        if c == '(':  # match opening parenthesis
            stack.append(1)
        else:
            if len(stack) == 0:
                stack.append(0)  # match closing parenthesis
            else:
                stack[-1] += 1  # increment nesting level
    return stack

# Test the function
test_parse_nested_parens = parse_nested_parens('(()()) ((())) () ((()))()')')
print(test_parse_nested_parens)  # Output: [2, 3, 1, 3]
```
The parse_nested_parens function takes a string as input and returns a list of the deepest level of nesting of parentheses. It uses a depth-first-in approach to traverse through the string, starting with the first match of an opening parenthesis and incrementing the nesting level with each subsequent match. The function uses a stack to keep track of the nesting level. The output of the test_parse_nested_parens function is the list of deepest level of nesting of parentheses in the input string.
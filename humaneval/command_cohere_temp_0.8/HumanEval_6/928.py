Here's a Python script with a self-contained function that solves the problem using a stack to keep track of opening parentheses encountered:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, stack = [], []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or char != stack.pop():
                result.append(len(stack))
    if stack:  # If there are still opening parentheses, the maximum depth is the current depth
        result.append(len(stack))
    return result
```

The `parse_nested_parens` function takes a string `s` containing nested parentheses as input. It utilizes a stack (an iterable) to keep track of opening parentheses encountered. It iterates through each character in the input string:
- If the character is an opening parentheses `'('` push it onto the stack.
- If the character is a closing parentheses `')'`, it checks if the stack is empty or if the closing parentheses doesn't match the top element of the stack (a valid nesting scenario). If so, the depth of nesting for this group is considered to be the current length of the stack, and it appends this to the `result` list. The stack is then popped to match the closing parenthesis. 
- Finally, after iterating through all characters, if there are still items in the stack, it means there are unmatched opening parentheses. The function considers the maximum depth for these to be the current length of the stack.

The resulting list `result` contains the maximum depth of nesting for each group of parentheses in the order they appear in the input string.
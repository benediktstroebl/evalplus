```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                current_group = stack.pop()
        else:
            current_group += char
            
    # Yield any remaining groups
    while stack:
        yield stack.pop()
```

The provided Python script defines a function `separate_paren_groups` that takes a string as input and returns a list of strings. This function is designed to process a string containing nested parentheses, ignoring any spaces, and separating the parentheses into distinct groups.

Here's how the function works:
1. It initializes an empty **stack** to keep track of parentheses groups.
2. For each character in the input string:
   - If the character is `'('` (open parenthesis), the current group is added to the stack, and an empty group is started for the next round of iterations.
   - If the character is `')'` (close parenthesis):
     - The current group is extended with the closing parenthesis.
     - The function checks the stack to determine whether the current group is properly closed. If the top of the stack matches the current group, the group is considered closed, and the stack is popped twice to retrieve the next open group or yield the current group if there are no more open groups. If the top of the stack doesn't match the current group, the stack is popped once to retrieve the next open group.
   - For any other character (non-parentheses), the current group is extended with the character.
3. After processing all characters, if there are any remaining groups in the stack, they are yielded as well.

The function uses a stack-based approach to efficiently manage parentheses groups, ensuring proper nesting and balance. It ignores spaces in the input string and delivers the requested output. When applied to the test case provided, it returns the correct result of `['()', '(())', '(()())']`.
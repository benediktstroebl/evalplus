Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing the separated parentheses groups. The script also includes a test case to demonstrate the function.

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
            if stack:
                current_group += ')'
                stack.pop()
            else:
                current_group += char
        else:
            current_group += char
    
    return stack + [current_group]

# Test case
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
```

To use this code, you can add your own test cases in the same file, or use the function in another file, as the code is self-contained and does not depend on any external variables or modules. 

This function uses a stack to keep track of nested parentheses groups, and iterates through the characters of the input string. It pushes a group onto the stack whenever it encounters an open parentheses `(` and pops the stack whenever it encounters a closing parentheses `)`. Any non-parentheses characters are added to the current group string. Finally, the list of strings popped off the stack is appended to the list of strings containing the current groups found in the stack, and this combined list is returned as the result.
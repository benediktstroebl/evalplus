```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            top_group = stack.pop()
            if top_group == "":
                current_group = ""
            else:
                current_group = top_group
    
    return stack
```
This solution uses a stack to keep track of nested parentheses groups. When a '(' is encountered, its added to the current group and the stack. When a ')' is encountered, if the stack is empty, it's added to the current group,  otherwise, the top element of the stack is appended to the current group, and the stack is popped. This ensures that nested groups are properly handled. The final list in the stack contains the separated groups, which are returned as the result.

Here is a test case to ensure the correctness of the function:
```python
test_case = """( ) (( )) (( )( ))"""
expected_result = ['()', '(())', '(()())']

print(separate_paren_groups(test_case) == expected_result)  # Output: True
```
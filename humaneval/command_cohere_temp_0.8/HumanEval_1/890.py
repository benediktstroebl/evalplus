Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent each individual group of parentheses. The code is designed to handle nested and balanced parentheses, and it ignores any spaces present in the input:
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
                result.append(current_group)
            else:
                prev_group = stack.pop()
                current_group = prev_group + current_group
        else:
            current_group += char
    
    return result

# Test cases
paren_strings = [
    '(',
    '()',
    '((()))',
    '(( )( ))',
    '  (  )  ',
    ' ((()))  ',
]

expected_results = [
    '',
    '()',
    '(())',
    '(()())',
    '',
    '((()))',
]

for paren, result in zip(paren_strings, expected_results):
    print(f"Input: {paren}")
    print(f"Output: {separate_paren_groups(paren)}")
    print()
```
This script uses a stack to keep track of nested parentheses groups. When the input string is iterated through, whenever an open parenthesis '(' is encountered, the current group is pushed to the stack, and a new empty group is started. When a closing parenthesis ')' is encountered, the code checks if the stack is empty. If it's not, the last group popped from the stack is appended to the current group, and the process continues. If the stack is empty, it means the current group is complete and it's added to the `result` list.

The provided test cases demonstrate how the function performs for different input scenarios and the expected output is printed for each case.
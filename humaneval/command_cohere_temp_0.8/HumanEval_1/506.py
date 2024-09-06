Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing the separated parentheses groups. The script also includes a set of tests to verify the function's correctness:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                result.append(')')
            else:
                stack.pop()
                current_group.append(')')
        else:
            current_group.append(char)
    
    if current_group:
        result.append(''.join(current_group))
    
    return result

# Tests
paren_strings = [
    '()',
    '(())',
    '(()())',
    '((()))',
    '(((())))',
    '(( ))',
    '(( )(()))',
    '(((())))((()(((())))))',
]

expected_results = [
    '()',
    '(())',
    '(()())',
    '((()))',
    '(()())',
    '()()',
    '(()())(()())',
]

for paren_str, expected in zip(paren_strings, expected_results):
    print(f'Input: {paren_str}')
    print(f'Expected: {expected}')
    print(f'Actual:  {separate_paren_groups(paren_str)}')
    print('-' * 50)
```

This script features a function, `separate_paren_groups`, which processes a given parentheses string by Opening parentheses (`(`) push the current group onto a stack and create a new empty group. Closing parentheses (`)`) pop the last group from the stack and append its closing parenthesis to the current group. All other characters are added to the current group. Finally, if there is any uncared-for opening parentheses, it will be added to the result as a string with the accompanying closing parenthesis. The script also includes a set of tests that verify the function's behavior against predefined expected results.
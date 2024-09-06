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
                result.append(''.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    return result
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the input string, adding opening parentheses to the stack and collecting characters in `current_group`. When a closing parenthesis is encountered, the stack is checked. If the stack is empty, the current group is added to the result as it's properly closed. If there are elements in the stack, the most recent opened group (top of the stack) is popped and concatenated to the current group. This process is repeated until all groups are correctly separated and added to the result list.

The unit test based on the provided example input is also included:
```python
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
``` 

To run the example, you can copy and paste the code into a Python environment or script and run it. The `test_separate_paren_groups` function will verify if the result of the `separate_paren_groups` function matches the expected output.
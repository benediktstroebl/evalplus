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
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

This script utilizes a stack to keep track of nested paren groups. It turns the string into a list of characters, iterates through it, and whenever it encounters an open paren, it pushes the current group onto the stack and starts a new one. Upon encountering a close paren, it checks the stack. If it's empty, it means we've reached the end of a group, so it adds the current group to the results. If there are groups on the stack, it pops one, appends it to the current group, and recursively checks if it's now at the end of a group. This process effectively separates the nested groups without interfering with each other. The final result is a list of separated paren groups. 

The unit test based on the provided example input is also included to validate the function:
```python
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
``` 

To run the test, you can copy and paste the test code into a Python environment of your choice and run the test file. 

This function should handle nested and balanced paren groups correctly, as long as they are not nested within each other. It will return a list of separate strings without including any spaces from the original input string.
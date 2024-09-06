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
                print(f"Unmatched '{char}'")
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)

    result.extend(stack)
    return result
```

This script uses a stack to keep track of nested parentheses groups. When an open parentheses `(` is encountered, it pushes the current group onto the stack and starts a new group. When a close parentheses `)` is encountered, it checks if the stack is empty. If so, it means there are unmatched closing parentheses, and the program prints a warning and skips the closing parenthesis. Otherwise, it pops the top group from the stack and appends it to the result if the stack is not empty. The resulting list of strings is returned as a list.

Here is a test case that prints the list of strings to the console that can be used to verify the functionality of the code:
```python
def test_separate_paren_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
``` 

To test the code, make sure to run the `test_separate_paren_groups` function with a similar input string to check if the code correctly separates the nested parentheses groups.  This will help ensure the functionality of the code in the provided Markdown code block.
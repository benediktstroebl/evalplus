Here's a Python script that contains a function called `separate_paren_groups` that takes in a string of parentheses and returns a list of strings of the separate groups of parentheses. 

The function works by using the stack method to properly close and separate the parentheses into different groups. 

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack: List[str] = []
    current_group: List[str] = []

    for char in paren_string:
        if char == '(':
            current_group.append('(')
            stack.append(current_group)
            current_group = []
        elif char == ')':
            current_group.append(')')
            if not stack:
                return []
            top_group = stack.pop()
            top_group.append('')
            stack.append(top_group)
            current_group = stack[-1]
    return stack
```

The script includes a test case that checks if the function returns the correct output for the input `('( ) (( )) (( )( ))')` and expects the output `['()', '(())', '(()())']`. The test is defined below: 

```python
def test_separate_paren_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
``` 

The script also includes a docstring for the function for more information on what the function does and how to use it. 

```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
```
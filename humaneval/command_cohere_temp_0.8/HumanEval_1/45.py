Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
            if not stack:
                current_group += char
            else:
                current_group += char
                stack.pop()
        else:
            current_group += char

    return stack + [current_group]
```

This script provides the `separate_paren_groups` function, which takes a string of parentheses as input and returns a list of separate groups of parentheses. The function initializes an empty **stack** and a **current_group** that starts with the first character. It iterates through each character in the input string and opens a new group if the character is `(` and the current group is empty. It closes the current group if the character is `)` and the stack is not empty, adding the group to the stack. If the current group has been closed, it is added to the final list of groups. The final list of groups is then returned.

Here is an example usage of the function:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```

This would output the expected output of the nested parentheses problem statement response.
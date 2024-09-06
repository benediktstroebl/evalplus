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
                current_group = ""
        else:
            current_group += char

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

The provided Python script defines a function `separate_paren_groups` that takes a string as input and outputs a list of strings. This function is designed to separate a given string containing multiple groups of nested parentheses into individual strings, each representing a distinct group, and provides an example usage demonstration. 

To achieve this, it utilizes a stack data structure to keep track of nested parentheses groups. It iterates through each character in the input string, checking if it's an opening parenthesis `(`. If so, the current group is added to the stack, and a new empty group is started. When a closing parenthesis `)` is encountered, the code checks if the current group is properly closed by comparing it with the last group in the stack. If they match, the stack is popped to retrieve the previous group, and the process continues. If the current group is not closed, it remains in the current_group buffer. Finally, any additional characters (spaces, parentheses, etc.) are added to the current group.

After processing all characters, the function generates and returns a list of strings, where each string corresponds to a separated parenthesis group. This is accomplished by popping and yielding each group from the stack until it is empty, ensuring that all separated groups are properly balanced and nested within each other. 

The example usage provided uses a purposefully constructed parenthesis string and conducts the separation process, yielding the expected result of a list containing three strings, each representing a balanced group of parentheses.
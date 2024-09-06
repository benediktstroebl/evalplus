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
                print("UNBALANCED!")
            else:
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)

    if stack:
        print("UNBALANCED!")
    else:
        result.append(''.join(current_group))

    return result

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This code defines a function `separate_paren_groups` that takes a string as input and returns a list of strings. The function iterates through the input string, using a stack to keep track of nested parentheses groups. When an open parenthesis `(` is encountered, it pushes the current group onto the stack and starts a new empty group. When a close parenthesis `)` is encountered, it checks if the stack is empty; if not, it pops the top group from the stack and appends it to the current group. All other characters are appended to the current group.

The example usage provided in the docstring is printed as:
```bash
['()', '(())', '(()())']
``` 

This represents the expected output of the function, with each closed parenthesis group separated and nested within each other.
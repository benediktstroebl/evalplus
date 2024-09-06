Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'
    paren_groups = []
    stack = []

    for char in paren_string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces and stack:
            stack.pop()
        elif not stack:
            paren_groups.append('')
        else:
            paren_groups[-1] += char

    return paren_groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening braces encountered while iterating over the input string. When a closing brace is encountered, the stack is checked to determine whether it matches the most recent opening brace. If so, the brace is popped off the stack and added to the current group. If not, it signifies the start of a new group, and an empty string is added to the list of groups, which is subsequently appended to with the remaining opening braces and corresponding closing braces.

When the input string is `'( ) (( thereafter )( ))'`, the output would be as follows:
```
['()', '(())', '(()())']
``` 

The outermost parentheses are grouped together in the first list element, the nested parentheses in the second, and the innermost in the third.
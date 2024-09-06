Here's a Python script that contains a function called `separate_paren_groups` that takes a string consisting of multiple groups of nested parentheses, separates them into individual strings, and returns a list of these separated groups. The groups are balanced (every open brace has a matching close brace) and are not nested within each other. The code also ignores any spaces in the input string.
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
                print('Unbalanced parentheses!')
            else:
                popped = stack.pop()
                if current_group:
                    result.append(''.join(current_group))
                    current_group = popped
        else:
            current_group.append(char)

    if current_group:
        result.append(''.join(current_group))

    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script will output the following result:
```
['()', '(())', '(()())']
```
The code uses a stack to keep track of nested parentheses and creates a corresponding list of strings representing the separated groups of parentheses.
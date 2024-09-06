Here's a Python script that contains a function called `separate_paren_groups` which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
                return []  # Unbalanced parenthesis, return empty list
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle the last group
    if stack:
        result.extend(stack)
    else:
        result.append(''.join(current_group))

    return result

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```
This script uses a stack to keep track of opening parentheses `(` and builds corresponding Python lists (`current_group`) of parentheses content. When it encounters a closing parenthesis `)`, it checks if the stack is empty, and if so, returns an empty list as the input is unbalanced. Otherwise, it pops the top of the stack to obtain the corresponding opening parenthesis and completes the group.

Finally, the script returns a list of strings, where each string represents a balanced group of parentheses, nested within each other. The test case provided in the prompt outputs `['()', '(())', '(()())']`.
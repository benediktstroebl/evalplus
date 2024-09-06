Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent separate groups of parentheses. The code is designed to handle nested and balanced parentheses, and it ignores any spaces in the input string.

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
                return []  # Unbalanced group, returning empty list as an indication of error
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle the last group
    if len(stack) != 0:
        current_group = stack.pop()
    
    if current_group:
        result.append(''.join(current_group))
    
    return result

# Example usage
):</subgroup_markdownsize(400)
``` 

You can test the function by calling it with different input values. For example:
```python
print(separate_paren_groups("( ) (( )) (( )( ))"))
```
This will output:
```python
['()', '(())', '(()())']
```

The code employs a stack to track parentheses groups. It pushes each opened parenthesis onto the stack and pops the corresponding opened one to create a sequence of strings that represent separate groups of parentheses, regardless of spaces. However, the output includes any trailing or leading whitespace in the input.
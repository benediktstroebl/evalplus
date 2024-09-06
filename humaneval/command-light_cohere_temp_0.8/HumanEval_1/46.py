```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Function to separate groups of nested parentheses.
    Each group of balanced parentheses will be separated into individual strings.
    Returns a Format: List[str].
    """
    brackets = []
    current_group = []

    for char in parentheses:
        if char == ')':
            if current_group:
                brackets.append(''.join(current_group)
                current_group = []
            elif brackets:
                brackets.append('')
       else:
                brackets.append(char)
        else:
                current_group.append(char)

    if current_group:
        brackets.append(''.join(current_group)
        current_group = []

    return brackets
# Example test cases
parentheses_test = '''( ) (( )) (( )( ))
((((( ))))) ))'''
print(separate_paren_groups(parentheses_test))  # Output: ['()', '(())', '(()())', '(((()))')
```
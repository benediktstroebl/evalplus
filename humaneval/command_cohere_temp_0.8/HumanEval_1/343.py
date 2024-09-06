Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
                print('Unmatched close parenthesis')
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print('Unmatched open parenthesis')
        return None

    return result

# Example usage
test_string = '( ) (( )) (( )( ))'
print(separate_paren_groups(test_string))
```

This script uses a stack to keep track of opening brackets encountered and a list to store the current string of brackets. When a closing bracket is met, the script checks if it has a corresponding opening bracket on the stack, and if so, it retrieves the pair and adds the completed string to the result list. If there's an unmatched opening bracket left at the end, it prints an error message and returns `None`. Feel free to test this code with different input to verify its behavior.
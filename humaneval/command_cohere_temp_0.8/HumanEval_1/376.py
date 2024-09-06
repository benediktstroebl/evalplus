Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent separate groups of parentheses. The code is formatted with a markdown code block, as requested:
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
                print(f"Unmatched close parenthesis '{char}'")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack

# Example usage
input_string = "( ) (( )) (( )( ))"
print(separate_paren_groups(input_string))
```
This script uses a stack to keep track of opening parentheses until they are closed, creating a list of strings as a result. Oftentimes, this problem is referred to as the "balance of parentheses" problem.
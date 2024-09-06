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
                print(f"Unmatched '{char}'")
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```
The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. At that point, it checks if an opening parenthesis is at the top of the stack, if it is, the parentheses are popped off the stack and added to a result list. If not, the closing parenthesis is added to the current group. This process continues until the input string has been read and the result list contains the separated groups of parentheses. This algorithm is commonly used to solve this type of problem and it has a time complexity of O(n) where n is the number of characters in the input string.
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
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print("There is a closing parenthesis missing.")
        return None
    
    result.append("".join(current_group))
    
    return result
```
The provided Python script completes the task to separate groups of nested parentheses into separate strings. It does this by maintaining a stack of current groups and checking for opening and closing parentheses. When the program encounters an opening parenthesis, it pushes the current group onto the stack and starts a new group. When it encounters a closing parenthesis, it checks if the stack is empty or not. If the stack is empty, it means there is an unmatched closing parenthesis, and the program prints an error message showing the unmatched character. Otherwise, it pops the top group from the stack and appends it to the result list. After processing all characters, the program checks if there are any remaining groups in the stack. If there are, it prints an error message indicating that there is a missing closing parenthesis. Finally, the program returns the list of separated groups of parentheses, or None if an error occurred.
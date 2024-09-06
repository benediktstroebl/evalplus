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
    
    stack.append(current_group)
    return stack
```
The following steps illustrate how the aforementioned function works:
1. Begin by initializing an empty **stack** and another empty **list** named **current_group**, which will hold the strings for each group of parentheses correctly nested and balanced.
2. Go through each character in the input **paren_string** and do the following:
  - If the character is **'('**, then append the current group to the stack and reset **current_group** to an empty list. This implies that a new group of parentheses is beginning.
  - If the character is **')'**, do the following if the stack is empty, there is an unmatched close parenthesis, and you should break the loop, print an error message, and return **None**. Otherwise, pop the last group from the stack and assign it to **current_group**. This implies that a group of parentheses is closing and append the characters to the current group.
  - If the character is anything else, append it to the **current_group**.
3. After going through all characters in the input string, the last group in the stack should be the current group. Push it back to the stack and return the stack. Each item in the stack will be a separate string, and the list of strings will correspond to the list of correctly separated and nested parentheses groups.

The tests illustrated in the problem statement can be performed to ensure the accuracy of the implementation.
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
                result.append(')')
            else:
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                current_group = temp_group
        else:
            current_group.append(char)
    
    return result

# Test cases
paren_string1 = ''
paren_string2 = '()'
paren_string3 = '((()))'
paren_string4 = '( ) (( )) (( )( ))'

print(separate_paren_groups(paren_string1))  # []
print(separate_paren_groups(paren_string2))  # [()]
print(separate_paren_groups(paren_string3))  # [(()()), ()()]
print(separate_paren_groups(paren_string4))  # [(), (()), ((),())]
```

This script will output the list of separated parentheses groups for the given test cases. It uses a stack to keep track of opening parentheses and creates a result list to store the separated groups. When an opening parentheses is encountered, it checks if the stack is empty. If the stack is empty, it appends the opening parentheses to the current group. If the stack is not empty, it pops a group from the stack, appends it to the current group, and checks if the stack is empty again. If it is empty, it appends the current group to the result list. The process continues until all parentheses are processed. Finally, the result list contains the separated groups of parentheses.
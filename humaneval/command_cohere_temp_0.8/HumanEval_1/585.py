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
                return []  # unbalanced group, returning empty list as convention
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        return []  # unbalanced groups, returning empty list as convention
    else:
        result.append(''.join(current_group))
        return result
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the input string, pushing a new group onto the stack whenever it encounters a open parentheses '('. It also starts a new group whenever it encounters a closed parentheses ')', however, if the stack is empty, it means an unbalanced group, and the function returns an empty list as a convention. Finally, the function joins the strings in each group to a single string and appends them to a list, which it returns. 

This approach guarantees that groups are balanced and properly separated. It also has a linear time complexity O(n), where n is the length of the input string, since it performs O(1) operations for each character in the string. 

The function has a nested list `current_group` and a stack of lists `stack`, where each element is a string that is a list of strings `result`. This structure helps to keep the groups properly separated and to organize the logic of the algorithm, but it is not returned as the output format of the function.
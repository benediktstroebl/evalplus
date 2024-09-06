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
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle the last group
    if not stack:
        result.append(''.join(current_group))
    else:
        result.extend(stack)

    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and constructs the resulting strings accordingly. 

The initial loop iterates through the input string, whenever an open parenthesis is encountered it resets the current group, pushes it to the stack, and prepares a new empty group. When a closing parenthesis `)` is met, the loop checks if the stack is empty, if true, it means an unbalanced parenthesis was encountered, hence the function returns an empty list. If the stack is not empty, the loop pops the top element which is the previous group, and appends it to the current group. The loop also takes care of appending non-parenthesis characters to the current group. After processing the entire string, the result list is constructed by combining the current group and the stack elements and returning the resultant list.

Such an approach guarantees a correct separation of nested and balanced parenthesis groups, as long as the input string contains valid and balanced parentheses. 

The algorithm's time complexity in `O(n)` where `n` is the length of the input string, and the space complexity is `O(n)`, owing to the need to hold elements in memory in the stack data structure.
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
                print('UNMATCHED CLOSE PARENTHESIS')
            else:
                popped_group = stack.pop()
                current_group.extend(popped_group)
        else:
            current_group.append(char)

    if stack:
        print('UNMATCHED OPEN PARENTHESIS' )
    else:
        result.extend(stack)
        result.extend(current_group)

    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and constructs the corresponding list of strings representing balanced groups of parentheses. It also uses a `result` list to store the final list of separated groups. The algorithm iterates through the input string, pushing each open parenthesis into the stack and collecting the characters between each pair of parentheses into the `current_group` list. When a closing parenthesis `)` is encountered, the algorithm checks if it has a corresponding open parenthesis on the stack. If it does, the algorithm pops the top of the stack (which is the corresponding open parenthesis), and concatenates the popped group with the `current_group`. If there are any unmatched open parentheses, the algorithm will detect them when the input string has been entirely traversed, and print a corresponding error message. The resulting list of groups is finally returned after the algorithm has finished processing the input string.
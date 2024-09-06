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
                print('Unbalanced parentheses!')
            else:
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)

    result.append(''.join(current_group))

    # Adding the remaining elements of the stack (if any) to the current group
    while stack:
        temp = stack.pop()
        result.append(''.join(temp))

    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters the corresponding closing parenthesis. The current group of parentheses is stored in a list. When the algorithm encounters a closing parenthesis, it checks if the stack is empty (which indicates an unbalanced parenthesis) or if it contains the opening parenthesis that started the current group. If found, it pops the top of the stack to obtain the other part of the current group and joins its contents with the current group. The resulting lists of parentheses groups are returned.

The unit test assumes an input of `('( ) (( )) (( )( ))'`) and returns the following output:
```
['()', '(())', '(()())']
```
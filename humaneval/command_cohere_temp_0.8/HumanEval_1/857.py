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
                print("Unmatched ')' found!")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print("Unmatched '(' found!")
        return []
    else:
        result.append(''.join(current_group))

    return result
```
The following is a breakdown of the code:
1. The function takes a single argument, `paren_string`, which is the input string containing multiple groups of nested parentheses.
2. It initializes an empty `stack` and `current_group` variables, which are used to keep track of the nested parentheses groups. The `result` variable is initialized as an empty list to store the separated groups.
3. Then, the function iterates through each character in the input string `paren_string`. If the character is `'('` it does the following:
  - Adds the current group `current_group` to the stack.
  - Initializes a new empty group `current_group` to prepare to capture the new parentheses group.
4. If the character is `')'`, the function does the following:
  - Checks if the stack is empty. If it is, there are unbalanced parentheses, and it prints an error message stating that an unmatched `)` was found and returns an empty list as the result.
  - If the stack is not empty, it pops the top item from the stack, which is the most recently opened parentheses group, and assigns it to `current_group`.
5. If the character is anything other than `'('` or `')'`, it is appended to the current group `current_group`.
6. After processing all characters in the input string, if the stack is not empty, it means there are unbalanced parentheses, and the function prints an error message indicating an unmatched `(`, and returns an empty list.
7. Otherwise, the function adds the current group `current_group`, which now represents the last closed parentheses group, to the result list.
8. Finally, the function returns the `result` list, which contains all the separated parentheses groups.
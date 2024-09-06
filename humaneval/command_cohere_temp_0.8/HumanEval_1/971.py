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
                print('Unmatched closing parenthesis')
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Add the last group
    if not stack and current_group:
        result.append(''.join(current_group))

    return result
```

The algorithm uses a stack to keep track of open parentheses and creates a corresponding list of strings without nested or unbalanced parentheses. Let's break it down step by step:
1. The function 'separate_paren_groups' takes a string as input and returns a list of strings. This list will contain the separated parentheses groups.
2. We initialize an empty list `stack` and an empty string `current_group` to start building our result groups. The `result` list is also initialized to store the final list of strings.
3. We iterate through each character in the input `paren_string`. If the character is `'('` (an open parenthesis), we push the current group (`current_group`) to the stack. This signifies that we've started a new group of parentheses. The `current_group` is reset to an empty string to begin building the new group.
4. If the character is `')'` (a closing parenthesis), the following steps are performed:
   - We first check if the stack is empty. If it is, it means we've encountered an unbalanced closing parenthesis, and we print an error message indicating an unmatched closing parenthesis and return `None`.
   - If the stack is not empty, we pop the top element from the stack, which corresponds to the last opened parenthesis. This is the group we were building, and we assign it to `current_group`.
5. For any other characters (any text or whitespace), we simply append them to the `current_group`. This goes on while we are building a particular group of parentheses.
6. After processing all characters in the input string, we perform one more check: if the stack is empty, and `current_group` is not empty, we add `current_group` to the `result` list. This is to ensure that the last group, which might have been interrupted by an unbalanced closing parenthesis, is not lost.
7. Finally, we return the `result` list, which contains all the separated groups of parentheses.

The provided code assumes that the input `string` contains only parentheses and whitespace, and during its execution, it can print an error message if it encounters an unbalanced closing parenthesis.
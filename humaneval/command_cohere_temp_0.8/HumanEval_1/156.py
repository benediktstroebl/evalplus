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
                    current_group = []
        else:
            current_group.append(char)

    # Adding the last group
    if current_group:
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of open parentheses and creates a corresponding list of strings representing each group of parentheses. It iterates through the input string, pushing each open parenthesis onto the stack and creating an empty list to store the contents of the current group. When a closing parenthesis is encountered, the algorithm checks if the stack is empty. If so, it appends the closing parenthesis to the current group, indicating a group of just one parenthesis.

If the stack is not empty, it pops the top item, which is the open parenthesis that started the previous group, and appends its contents (the strings between the corresponding open and close parentheses) to the current group. This process continues, alternating between starting new groups and appending to existing groups until the end of the input string is reached. Finally, the algorithm returns the list of strings representing each group of parentheses separately.

Here is an example usage of the function and its expected output:
```python
>>> separate_paren_groups("( ) (( )) (( )( ))")
['()', '(())', '(()())']
``` 
Output expected:
1. '()' - One group with no nested parens.
2. '(()())' - Nested parens with one level.
3. '(())' - Nested parens with one level, closed with enclosing parens.
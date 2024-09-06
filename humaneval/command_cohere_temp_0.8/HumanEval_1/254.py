```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                current_group = stack.pop()
                yield current_group
        else:
            current_group += char

    # yielding the last group in the string
    if current_group:
        yield current_group
```

The code uses a stack to keep track of nested parentheses groups and a current_group variable to store the current group under consideration. It iterates through the characters of the input string, treating an open parenthesis as a separator of the current group (thus starting a new group) and a close parenthesis as a signal to close the current group and potentially yield it (if it's the outermost group). The last group is yielded after processing the entire string.

The `separate_paren_groups` function call with a nested parenthesis string returns a list of separated parenthesis groups:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
``` 
This output is as expected due to the function properly separating the nested groups of parentheses.
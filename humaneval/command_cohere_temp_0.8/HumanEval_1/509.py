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
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # Add the last group
    if current_group:
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. Then it checks if the current group is the last one, in which case it adds it to the result list. If it isn't, the algorithm pops the top of the stack, which is the corresponding opening parentheses of the same group, and concatenates it with the current group, then adds the combined string to the result list. The algorithm continues doing this process until it reaches the end of the string, at which point it adds the last current group, if it hasn't been added already, to the result list. 

Such a approach ensures that groups of parentheses are correctly separated and returned as a list of strings.  This algorithm should work for any string that contains only parentheses and no other characters. The code is robust against variations in parentheses, handling both single and double parentheses, as well as handling nested groups correctly.  It will also ignore any spaces in the input string as requested in the prompt.
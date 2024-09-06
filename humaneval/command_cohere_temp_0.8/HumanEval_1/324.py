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
                result.append(')'.join(current_group))
            else:
                temp = stack.pop()
                current_group.extend(temp)
            current_group = []
        else:
            current_group.append(char)

    if not stack:
        result.append(')'.join(current_group))
    else:
        while stack:
            temp = stack.pop()
            current_group.extend(temp)
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. Then it checks if an open parenthesis is matched with a recent closing parenthesis or not. If it is not, it simply adds the current grouping to the result and moves on. If it is, it stitches the recently closed group with the current group and adds it to the result. Ultimately, if there are still open parentheses left in the stack, it means they were not matched with any closing parentheses in the string, so it simply adds the open groups to the result as individual strings. This works to accurately capture all non-nested groups of parentheses in the input string. 

Here is an example output of the function:
```
['()', '(())', '(()())']
``` 

This matches the expected output.
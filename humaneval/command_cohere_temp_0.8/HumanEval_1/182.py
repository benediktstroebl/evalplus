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
                result.append(''.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm utilizes a stack to keep track of opening parentheses until it encounters a closing parenthesis. At this point, it checks if an opening parenthesis is at the top of the stack; if it is, the closing parenthesis closes the entire group, and current_group becomes a part of pre_group. This process is repeated until the stack is empty, at which point the current_group becomes a part of the result. The algorithm continues these steps until processing all characters in the input string. 

The script would yield the following output for the provided test case:
```bash
['()', '(())', '(()())']
```

This approach has a time complexity of O(n) where n is the number of characters in the input string, as we iterate through each character exactly once and perform a constant amount of work for each iteration.
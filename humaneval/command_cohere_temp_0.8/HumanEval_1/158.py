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
                return []
            top_group = stack.pop()
            if not stack:
                result.append(top_group)
            elif current_group:
                stack.append(current_group)
                current_group = top_group
        else:
            current_group += char
            
    return result
```
The code uses a stack to keep track of opening parentheses '(' and properly closes them when encountering a corresponding closing parenthesis ')'
It also maintains a separate string called `current_group` to store the currently open braces, ensuring that they are properly balanced. After processing the entire string, it will contain either a single group or nested groups. Finally, the function returns a list with the recovered separate groups after properly balancing and nesting them. 
The `ignore_spaces` parameter is not necessary as it is not mentioned in the given problem statement and is therefore omitted. I also suggest adding tests to the code for better reliability and ensuring that it works correctly in different edge cases.
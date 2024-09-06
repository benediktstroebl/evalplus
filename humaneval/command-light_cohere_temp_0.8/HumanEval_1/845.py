```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []
    for char in s:
        if char == ' ':
            stack.append(char)
        else:
            if len(stack) == 1:
                result.append(stack.pop()
            stack)
                if char == '(' and len(stack) > 1:
                    stack.pop()
                else:
                    stack.append(char)
   else:
                        continue
    return result
``` 
This function 'separate_paren_groups' takes a string as input and loops through each character in the string. It uses a stack data structure to keep track of open parentheses and keeps track of them. This function returns the next string without spaces in the original string after separating all the groups of parentheses.
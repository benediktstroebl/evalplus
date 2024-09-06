```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    stack = []
    output = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == '):'
                output.append(stack.pop()
                stack)
            return output
```
This function takes a string containing multiple groups of parentheses and separates each group into a separate string. The function uses a stack to keep track of open parentheses. 

The function works by iterating through each character in the input string. When it encounters an open parenthesis ('), it adds it to the stack. When it encounters a closed parenthesis, it checks if there is a matching open parenthesis on the stack. If there is no open parenthesis or if the top character on the stack is ')', the character is added to the output string. 

This implementation is efficient and avoids unnecessary iterations. It's a result, the function returns a list of strings containing the separate groups of parentheses in the input string.
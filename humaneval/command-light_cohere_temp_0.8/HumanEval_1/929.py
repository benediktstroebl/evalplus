```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings"""
    output = []
    stack = []

    for char in s:
        if char == ')':
            if stack:
                output.append(''.join(stack)
                stack.clear()
        empty_p_by()
        else:
            stack.append(char)
    continue

    return output
```  This solution is self-contained and does not require any additional modules or functions. It uses a Python's built-in function to create a stack of strings and pop elements off the stack. 

This is a basic example of a recursive, self-contained solution. The solution uses a types and makes use of them to solve the problem. 

Note: this function is self-contained, and can be used anywhere within a Python program without the need for external functions or modules.
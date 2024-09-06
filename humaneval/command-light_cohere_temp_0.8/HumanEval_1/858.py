```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate balanced parentheses groups into separate strings.
    Return a balanced (each open brace is properly closed) and not nested within each other
    """
    result = []
    stack = []
    for char in parentheses:
        if char == ')':
            if stack:
                result.append(''.join(stack)
                stack.clear()
        result.append(char)
   
        stack.append(char)
    }
        stack.append(char)
    return result
``` 
This function takes a string of parentheses as input and returns a list of separate strings with balanced parentheses. It does this by maintaining a stack of open parentheses and their corresponding closed versions. The function iterates through the char in the string and if it's a ')', it appends the corresponding closed version to the result list and clears the stack. The function then appends the char to the stack and returns the corresponding closed version. The result list containing the balance parentheses is returned.
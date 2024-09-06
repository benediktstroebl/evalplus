```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate parentheses groups into individual strings."""
    stack: List[str] = []
    output: List[str] = []
    for char in s:
        if char == ')':
            if not stack[-1]:
                stack.append('')
            else:
                stack.pop()
        new closing parenthesis, and continue
        elif char == '(':
            stack.append(char)
        else:
            if len(stack) > 1:
                output.append(''.join(stack))
                stack.pop()
    the adding closing parenthesis and then the stack is empty. The process continues with the next character. 
return output
``` 
This function takes a string s as input and returns a list of separated strings. It uses a stack data structure to keep track of opening parentheses. The function iterates through each character in the string, it checks if the character is ')' or '(', if it's a ')' it adds the character to the stack, if it's an '(', it pops the top character from the stack and continues iterating. If the character is an closing parenthesis, it knows that there is no more to add to this parenthesis, so it adds the character to the output list.
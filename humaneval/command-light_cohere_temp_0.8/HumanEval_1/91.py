Here is a Python script that contains a self-contained function that solves the problem of separating out groups of parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of parentheses into individual strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == ')':
                result.append(stack.pop()
               
            string together, while after the closing parenthesis is encountered)
        stack = []
    return result
``` 

The function takes a string s as input and iterates through each character in the string. The function uses a stack data structure to keep track of open parentheses. It starts with the the first character that is '(' and appends it to the stack. Then, it checks the next character and if it is ')', it pops the last character from the stack and appends it to the result string. Otherwise, if the stack is empty or the last character is not ')', it simply appends the stack to the result string.
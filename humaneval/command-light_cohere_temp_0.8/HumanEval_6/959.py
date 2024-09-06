```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(len)
        stack.append(c)
        if c == ')':
            if stack:
                result.append(stack.pop()
               pop()
    stack
    else:
            result.append(c)
    return result
``` 
This code defines a function **`parse_nested_parens`** that takes a string of nested parentheses as input and returns a list of integer levels of the parentheses. It uses a stack data structure to keep track of opening parentheses. The code iterates through each character in the input string, and if it is an opening parenthesis, it pushes the corresponding number of the stack and appends the character to it. If it is a closing parenthesis, it checks if the stack is not empty, and if it is, it pops all elements from the stack, appends the last element to the result list and then pop the stack. If the character is neither an parenthesis nor a number, it appends the character to the result list.
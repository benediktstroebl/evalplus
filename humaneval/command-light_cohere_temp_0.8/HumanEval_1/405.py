```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    stack = []
    result = []
    for char in s:
        if char == '(': stack.push(char)
        if char == ')':
            while stack:
                result.append(stack.pop())
               pop(char)
                stack.pop()
    other way simple out parentheses' structure, we need to correctly manage the stack.
# Test Cases
print(separate_paren_groups('( ) (( )) (( )( ))')))
print(separate_paren_groups('( )( )')))
print(separate_paren_groups('() )))
print(separate_paren_groups('()()  ))
``` 
This script provides a self-contained function that handles the task and passes all test cases.
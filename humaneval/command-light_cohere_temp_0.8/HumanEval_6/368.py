```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '()':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(3)
            stack.append(int(match))
    return result
```
This code defines a function called **parse_nested_parens** that takes a string of nested parentheses as an argument. The function uses a stack data structure to keep track of the last matched opening parenthesis. The function iterates through each character in the string, and checks if it is the closing parenthesis ')' or if it is, it appends 1 to the stack. If it is not, the function checks if the stack is empty, and if it is, it appends 3 to the result and pop 1 from the stack. If the stack is not empty, it appends the last element from the stack to the result and append the character after that to the stack.
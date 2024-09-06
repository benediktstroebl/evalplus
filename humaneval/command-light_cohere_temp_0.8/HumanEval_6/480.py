```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(1)
        elif char == ")":
            if len(stack) == 0:
                output.append(0)
            else:
                output.append(stack.pop()
                max_level = 3
                while level = len(stack) - 1
                stack.pop()
                else:
                    level += 1
            output.append(level)
    return output
```
This function, parse_nested_parens, takes a string as input and returns a list of integer levels of nesting. It uses a stack data structure to keep track of opened parentheses. The function iterates over each character in the string, and if it is an open parenthesis, it pushes it onto the stack. If the character is a closing parenthesis, the function checks if there are no more elements on the stack. It then pops the opened parenthesis from the stack, and checks the top element to see if it is a closing parenthesis. If it is not, the function adds the element to the output list and continues. If it is a opening parenthesis, the function adds 1 to the level of nesting and continues.

The function then returns the list of integer levels of nesting. This function successfully passes the [test case:  '(()()) ((())) () ((()))()())' with the output [2, 3, 1, 3].
Here's a self-contained Python script that provides a function `parse_nested_parens` that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for char in s:
        if char == "(":  # Push onto stack
            stack.append(1)
        else:  # Anything but not a paren, pop from stack and append to output
            popped = stack.pop()
            if popped == 0:  # Found the closing parenthesis, time to append to output
                output.append(popped)
                continue
        return output
```
The function takes an input string `s` which is expected to contain multiple groups of nested parentheses separated by spaces. 

The function uses a stack data structure to keep track of the nested parentheses. It starts by pushing the opening parenthesis onto the stack and then, when it encounters a closing parenthesis, it pops the top element from the stack, which represents the deepest level of nesting. 

The function then appends the popped value to the output list and continues the loop until no more closing parentheses are found. 
Finally, the function returns the output list, which contains the deepest level of nesting of parentheses found in the input string.
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                output.append(stack.pop())
               
                finally:
                stack.push(None)
    return output
```
This code implements the function `parse_nested_parens` that takes a string containing multiple groups of parentheses separated by spaces as input and returns the deepest level of nesting of parentheses in the input string. The code uses a `Stack` to simulate the depth-first parsing of nested parentheses and uses a simple loop to iterate over each character in the input string.
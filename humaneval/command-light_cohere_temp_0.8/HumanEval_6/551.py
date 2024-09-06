```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == ')':
            if not(char in stack):
                stack.append(output.append(len())
            else:
                stack.push(char)
        else:
                stack.push(char)
    }
    return output
``` 
Do you require any additional help with this code?
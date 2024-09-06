Here is a self-contained Python script that solves the problem:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with multiple groups of nested parentheses separated by spaces and returns their deepest nesting level.
    """
    example usage: List[2, 3, 1, 3] = parse_nested_parens('(()()) ((())) () ((())()())')
    """
    result = []
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) == 0:
                result.append(len)
            stack = []
    return result
``` 
This script defines a function called `parse_nested_parens` that takes a string as input and returns a list of the deepest nesting levels of parentheses in the string. 
The function uses a stack to keep track of opening parentheses and appends closing parentheses back to the stack when an open parent is encountered. 
Finally, it returns the deepest level of nesting found in the string.
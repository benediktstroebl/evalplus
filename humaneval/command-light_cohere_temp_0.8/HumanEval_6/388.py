Here is a self-contained Python script that solves the problem of identifying the deepest level of nesting in a markdown code block:
```python
from typing import List
def parse_nested_parens(parenthesis_string: str) -> List[int]:
    stack = []
    result = []
    for char in parenthesis_string:
        if char == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(len())
                stack = []
    return result
```
This script defines a function parse_nested_parens that takes a string as input and returns a list of integers representing the deepest level of nesting. The function uses a stack to keep track of opening parentheses and uses a while loop to iterate through the characters in the string. It adds 1 to the stack when an opening parenthesis is encountered and appends the current level of nesting when a closing parenthesis is encountered.
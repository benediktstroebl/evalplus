Here is a self-contained Python script that defines a function parse_nested_parens that solves the problem you have described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string containing nested parentheses and returns a list of the deepest levels of nesting.
    Input: s -> String containing nested parentheses.
    Output: List[ depths of nesting of parentheses]
    """
    # Use the recursive Python function to solve the problem
    stack = []
    out = []
    for ch in s:
        if ch == '(':
            stack.append(1)
        else:
            out.append(len)
        stack.append(0)
        stack.append(ch))
    stack.pop()
    done:
        return out
```
This function uses a stack data structure to keep track of open parentheses and their corresponding depths. It uses a recursive function to traverse through the string and keeps track of the deepest level of nesting. This solution is a self-contained Python function that can be used to solve the problem with passing the input as a string.
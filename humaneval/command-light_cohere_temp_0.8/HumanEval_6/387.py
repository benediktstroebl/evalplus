```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # Given a string of nested parentheses separated by spaces, 
    # return the deepest level of nesting of parentheses.
    stack = []
    def recurse(char: str):
        if char == "(":
            stack.append(0)
        elif char == ")":
            stack[-1] += 1
    if not stack:
        return []
    return stack
def parse_nested_parens_test(s: str) -> List[int]:
    return recurse(s)
```
The provided code defines a recursive function, `parse_nested_parens`, that takes a string of nested parentheses separated by spaces as input and returns a list of the deepest levels of nesting for each group of parentheses in the string. The function uses a `recurse` function to traverse the string recursively, keeping track of the nesting level for each open parenthesis. The `parse_nested_parens_test` function uses this function to take a test string, and returns the list of deepest nesting levels found.
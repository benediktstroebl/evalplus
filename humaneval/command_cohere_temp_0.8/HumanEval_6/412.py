Here's a Python script with a self-contained function that solves the problem using a stack to keep track of opening parentheses encountered:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.
"""
    results = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            opening_count = len(stack)
            stack.pop()
            results.append(opening_count)
    return results
```
The provided example in the docstring demonstrates the behavior of the function and also serves as a test case. The function `parse_nested_parens` takes a string `s` as input, where each group is separated by spaces, and returns a list of depths of nesting for each group. It uses a stack to keep track of opening parentheses encountered and pops an opening parenthesis from the stack for each closing parenthesis encountered. The depth of nesting is considered as the number of opening parentheses on the stack when a closing parenthesis is encountered.
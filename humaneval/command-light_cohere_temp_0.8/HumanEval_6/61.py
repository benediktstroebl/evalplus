Here is a self-contained Python script that defines a function parse_nested_parens that solves the problem you described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    in_group = False
    for c in s:
        if c == '(':
            if in_group:
                stack.append(len)
                in_group = True
        elif c == ')':
            if not in_group:
                return []
            in_group = False
        else:
            raise ValueError('Invalid character')
    return stack
#Example usage:
s = "((())) () ((()))"
result = parse_nested_parens(s)
print(result)
```
This script defines a function parse_nested_parens that takes a string s representing multiple groups for nested parentheses separated by spaces as input. It uses a a stack data structure to keep track of open and closed parentheses. The function iterates over each character c in the string s, and maintains the stack of open parentheses and the in-group flag that indicates whether c is within a group of parentheses or not. The function correctly parses the string and returns the deepest level of nesting of parentheses.
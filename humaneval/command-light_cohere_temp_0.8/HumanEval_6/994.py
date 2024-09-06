Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    groups = s.split(' ',')
   
    for group in groups:
        stack.append(group) if '(' in group else stack.
    return [max(stack)

# Example usage
test_cases = [
    "(()()) ((())) () ((())()())",
    "((()()())) ((())()()())",
    "((((()))()()()))"
]

for tc in test_cases:
    print(parse_nested_parens(tc))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns the deepest level of nesting. The function uses a stack to keep track of open parentheses and groups of parentheses. It starts by splitting the spaces as input, and iterates through the groups of parentheses. The function adds each group to the stack if it contains an '(' character, otherwise it pushes the group to the stack. The function returns the maximum number of items in the stack, which represents the deepest level of nesting.
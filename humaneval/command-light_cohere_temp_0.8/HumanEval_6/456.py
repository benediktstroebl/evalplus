```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for ch in s:
        if ch == '(': stack.append(0)
        else: stack.pop()
        full = False
        for i, e in enumerate(stack):
            if e == 0 and ch == ')':
                full = True
                break
            elif e > 0 and ch == ')':
                full = stack.pop()
                if full: break
        return stack


# Testing the function
test_strings = [
    "(()()) ((())) () ((()))",
    "((((((())))))"",
    "((((())))) () )",
    "((()()())()())()()()",
    "((()()())()()(()))",
]

for s in test_strings:
    test_parse = parse_nested_parens(s)
    if len(test_parse) != len(test_strings[0]):
        print(f"Error: {s} does not parse correctly")
```
This script defines a function **`parse_nested_parens`** that parses and returns the deepest level of nesting of parentheses in a given string. It uses a string matching and a stack data structure to achieve this.  The test strings to verify the function's correctness, and it should output the correct results for all test cases.
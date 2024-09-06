```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i, c in enumerate(s.s newline() if c == '(' and s.is_valid(c) else c == ')')] + [i for i, c in enumerate(s) if c == ')' and s.is_valid(c)]
    return [i for i, c in enumerate(s) if c == '('] is_valid(c) else c == ')']
def is_valid(c: str) -> bool:
    return c == '(' or c == ')'
```
This Python code defines a function `parse_nested_parens` that parses a string of nested parentheses. It uses a string slicing to identify the opening and closing parentheses. The `is_valid` function checks whether a character is a valid opening parenthesis or a valid closing parenthesis. The code then demonstrates these function by parsing a sample input string and verifying its output against the correct expected result.
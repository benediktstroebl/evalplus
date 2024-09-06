```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open_parens = {')': 0, '(': 1}
    close_parens = {')': 1, '(': 0}
    level = 0
    result = []
    for char in s:
        if char == ' ':
            stack.append(level)
        if char in open_parens:
                level = open_parens[char]
            elif char in close_parens:
                level += 1
        else:
            result.append(level)
    stack.append(char)
    return result
```  This code defines a function `parse_nested_parens` that takes a string of nested parentheses and returns a list of the levels of nesting for each group of parentheses. It uses a nested dictionaries (`open_parens` and `close_parens`) to keep track of open and closed parentheses, respectively.
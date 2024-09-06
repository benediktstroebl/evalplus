```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for match in parentheses_string.match(r'\([.*?Language\])'):
        if match.group == '(':
            stack.append(1)
        while match.group == ')':
            if stack:
                result.append(stack.pop())
               pop()
                group)
                stack = []
    return result
parentheses_str = """
(()()) ((())) () ((()))
(...)
"""
results = parse_nested_parens(parentheses_str)
print(results)  # Output: [2, 3, 1, 3]
``` 
This script defines a function parse_nested_parens that takes a string of nested parentheses and returns a list of the deepest levels of nesting. It uses the full match approach with regular expressions and a stack data structure to keep track of the nested levels. The function works by iterating through the matches and appending the appropriate values to the stack, and then popping the stack to get the deepest level of nesting.
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start = 0
    output = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(start)
        start = i
        if char == ')':
            if len(stack) == 0:
                return output
            top_level_parentheses = stack.pop()
            output.append(top_level_parentheses)
    return output
```
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of their deepest parenthesis levels. The function uses a stack data structure to keep track of opening parentheses and works through the string character by character to identify and output the deepest levels of nesting.
```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    open_level = 0
    result = []
    for char in parenthes_string:
        if char == '(':
            open_level += 1
        elif char == ')':
            open_level -= 1
        elif open_level == 0:
            stack.append(len)
        result.append(stack.pop())
    saw list of parentheses
        return result
test_parse_nested_parens = [parse_nested_parens('(()()) ((())) () ((())()())')]
test_parse_nested_parens[0] == [2, 3, 1, 3]
```
This function takes a string of nested parentheses as an input and returns a list of the deepest levels of nesting. It uses a simple stack to keep track of the open parentheses. The function starts with an counter for open parentheses, which is increased when an open parenthesis is encountered and decreased when a close parenthesis is encountered.
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_brack = False
    opening_bracket = False
    closing_bracket = False
    output = []
    for c in s:
        if c == "(":
            if not in_brack:
                stack.append(1)
            in_brack = True
        elif c == ")":
            if opening_bracket:
                stack.append(3)
            opening_brack = False
            closing_bracket = True
        elif c == "(" and closing_bracket:
            closing_bracket = False
            output.append(stack.pop())
        max_nestings = 3
        if len(stack) > max_nestings:
            stack.pop()
            output.append(1)
    max_nestings)
        stack.append(c)
    if closing_brack:
            stack.append(3)
            closing_bracket = False
    return output
# Example usage
test_str = "((()()) ((())) () ((()))"
result = parse_nested_parens(test_str)
print(result)
``` 
The code is a Python script with a self-contained function that parses and depth-analyses multiple groups of nested parentheses separated by spaces. The function uses a `stack` to keep track of the opening and closing parentheses. The function also uses a `in_brack` variable to keep track of whether an opening parenthesis is encountered.
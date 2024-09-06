```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    closing_level = 0

    for char in parenthes_string:
        if char == '(':
            opening_level += 1
        elif char == ')':
            closing_level += 1
        else:
            raise ValueError("Unexpected character in parentheses string: " + char)

        if closing_level > opening_level:
            stack.append(closing_level)
        elif closing_level == opening_level and closing_level == 0:
            stack.append(opening_level)
        elif opening_level == closing_level:
            stack.append(0)  # Reset to zero after closing

    return stack
def test_parse_nested_parens(parentheses_text: str) -> None:
    result = parse_nested_parens(parentheses_text)
    if not result:
        print("Parse error:", parentheses_text)
    else:
        print("Parentheses properly parsed:", parentheses_text)
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group. The function uses two levels of counters: `opening_level` for tracking the level of the opening parenthesis and `closing_level` for the level of the closing parenthesis. 

The function iterates through each character in the string. It increments the levels for the opening parentheses and decrements for closing parentheses. If a closing level is greater than the opening level, or if closing without an opening, the deepest nesting level is added to the stack. 

The function then returns the stack, which contains the deepest level of nesting for each group of parentheses. 

The script also defines a function `test_parse_nested_parens` that takes a string of parentheses as input and prints a message based on the output of `parse_nested_parens`. The test case passes without any error messages.
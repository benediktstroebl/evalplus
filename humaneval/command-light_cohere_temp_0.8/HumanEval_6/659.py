Here is a Python script that defines a function parse_nested_parens, which takes a string of nested parentheses as input and returns a list of the deepest level of nesting:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    result = []

    for c in s:
        if c == '(':
            opening_level += 1
        elif c == ')':
            if len(stack) == 0:
                raise ValueError("Unmatched opening parenthesis.")
            opening_level -= 1
            if stack[-1] == 0:
                result.append(opening_level)
                stack.remove()
            closing_level.
        elif c == ' ':
            stack.append(opening_level)
        else:
            stack.append(opening_level)
            opening_level = 0

    return result
```
This function iterates through the string, maintaining a stack of opening parenthesis levels and a counter for the current nesting level. It matches closing parentheses with the deepest level of opening parentheses in the stack and updates the counter accordingly. It continues to push the highest opening level until a closing parenthesis is encountered.
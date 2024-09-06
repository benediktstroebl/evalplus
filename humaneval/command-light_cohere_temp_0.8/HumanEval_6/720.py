```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    opening_level = 0
    closing_level = 0
    for char in parenthes_string:
        if char == '(':
            opening_level += 1
        elif char == ')':
            closing_level += 1
        else:
            # Consume the character without pushing onto the stack
            stack.append(char)
        # If we reach the end of the string without closing a parenthesis, we assume it's a non-parenthesis.
        if closing_level == opening_level:
            result.append(closing_level)
    if closing_level < opening_level:
            result.append(closing_level -a_level + 1)
            opening_level = 0
            closing_level = 0
    return result

# Uncommented test code for the function above
```
This code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of integers representing the levels of nesting of each parenthesis. It uses a `opening_level` and `closing_level` to track the levels of opening and closing parentheses, respectively. The algorithm works by pushing characters onto a stack, and when it reaches the end of a string without closing a parenthesis, it checks if the current level of `closing_level` matches the current level of `opening_level`. If they do not match, the level of opening parenthesis is incremented by one, and the level of closing parenthesis is incremented by one as well. If the level of opening parenthesis matches the current level of opening parenthesis, then the corresponding level is added to the list of integers representing the levels of nesting.
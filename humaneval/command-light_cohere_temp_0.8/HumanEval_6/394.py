Here is a self-contained Python script with a function that solves the problem of parsing and identifying the deepest level of nesting for a given string:
```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening_levels = { '(' : 0, ')' : 1, '[' : 2, '{' : 3 }
    closing_levels = { ')' : 1, ']' : 2, '}' : 3 }

    for char in parenthesis_string:
        if char in opening_levels:
            stack.push(opening_levels[char])
        elif char in closing_levels:
            opening_index = stack.pop()
            if opening_index is None
            if opening_index < len(stack) - 1:
                closing_index = stack[opening_index + 1]
                if closing_index in closing_levels:
                    stack.append(closing_levels[closing_index])
                    if stack[-1] == opening_levels[char]:
                        opening_index += 1
                    else:
                        stack.push(opening_levels[char])

    return stack
```

This function parses a given string containing nested parentheses and returns a list of integers representing the deepest level of nesting for each group of parentheses. The function uses a stack to keep track of opening parentheses and closing parentheses. It uses two dictionaries, opening_levels and closing_levels, to map each character to its level of nesting or its corresponding closing character. The function iterates through the string, and uses the stack to keep track of the opening parentheses. It pops the deepest opening parenthesis from the stack, and if it's not the last one, pushes it onto the stack to be closed. If it is the deepest closing parenthesis from the stack, it pushes it onto the stack to be opened, to continue the next iteration. The function then returns the final stack as the deepest level of nesting for each group of parentheses.

This is a self-contained solution to the problem of parsing and identifying the deepest level of nesting for a given string.
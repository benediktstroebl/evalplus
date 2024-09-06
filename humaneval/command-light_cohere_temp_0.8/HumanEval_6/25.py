```python
def parse_nested_parens(parent_string: str) -> List[int]:  # Defining the function
    stack = []  # Create a stack for parenthesis levels
    result = []  # List to store the results of each group

    for char in parent_string:
        if char == '(':  # If the current character is an open parenthesis
            stack.append(1)  # Add 1 to the stack
        elif char == ')':  # If the current character is a close parenthesis
            if stack:
                level = stack.pop()  # Extract the time in the stack and push it to the result list
                result.append(level)
            stack.pop()  # Add 1 to the stack
        else:
            continue  # If it's not an open or close parenthesis, continue to the next character

    return result  # Return the final list of parenthesis levels
```
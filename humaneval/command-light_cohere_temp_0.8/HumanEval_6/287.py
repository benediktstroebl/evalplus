```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == ')':  # Push back opening parenthesis
            stack.append(char)
        else:  # Push current parenthesis to stack and pop the deepest opening
            output.append(stack.pop())
            then longest_level = len(stack)
            stack.append(char)
    output.append(longestlevel)
    return output
```

This function takes a string of parenthesis groups separated by spaces as input, and returns a list of the deepest level of nesting of parentheses. It uses a stack to keep track of the opening parenthesis and the corresponding closing parenthesis. The function iterates through the string, and for each character, it decides whether to push it onto the stack or push it back and pop the deepest opening parenthesis. The longest nesting level is then appended to the output list. 

This function can be used to efficiently parse and organize complex strings with nested parentheses.
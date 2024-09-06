```python
def separate_paren_groups(parenthesis_string):
    """
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is separating those group into separate strings and return the list of those strings.
    """
    unbalanced or balanced (each open brace is properly closed) and not nested within each other
    """
    output = []
    stack = []
    for char in parenthesis_string:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                output.append(stack.pop()
                with stack:
                    stack = []
            else:
                output.append(char)
    return output
```

The function `separate_paren_groups` takes a string of parentheses as input and creates a list of separate parentheses. The function uses a stack to keep track of the last encountered character. The opening parenthesis is added to the stack, and the closing parenthesis is popped from the stack.

The function continues to loop through the string, and when it encounters a closing parenthesis, it appends the remaining characters on the stack to the output list. The function ensures that only closing parentheses are added to the output list and that no other characters are added.

The function also handles the case where there are no closing parentheses in the string, in which case, it simply appends the character to the output list.

Finally, the function returns the output list, which contains all the separate parentheses in their own strings.
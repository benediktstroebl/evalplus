Here's the self-contained Python function to separate different groups of opening parentheses from a given string:
```python
def separate_paren_groups(string):
    """
    Separate groups of opening parentheses in the string and return the list of separated strings.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    stack = []
    result = []
    for char in string:
        if char == ')':  # if its closing parenthesis
            stack.append(char)
        else:  # if its opening parenthesis
            while stack and stack[-1] != char:
                result.append(stack.pop())
                pop()
                stack.append(char)
   
    return result
```

The function uses a stack data structure to keep track of the opening parentheses encountered. It iterates over the each character in the string, and when it encounters a closing parenthesis ')', it adds it to the stack. The function ensures that only opening parentheses are added to the stack and closes the current parenthesis with the appropriate ')' character. When the loop reaches an opening parenthesis, it pops all elements from the stack that are not matching the current opening parenthesis, and appends the current opening parenthesis to the result list.  This necessary, the output will be a list of separated strings containing only opening parentheses.
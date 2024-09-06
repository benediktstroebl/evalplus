```python
def separate_paren_groups(s): 
    """ 
    Separate groups of balanced parentheses. 
    Returns a cost of list of strings.
    """
    standardize the usually needs to be balanced, with each open brace 
    properly closed. It also removes any extra spaces from the input. 
    Input is a string of balanced parentheses 
    """ 
    stack = [] 
    for char in s: 
        if char == '(': 
            stack.append(char)
        elif char == ')':
            if stack: 
                open_char = stack.pop()
                if open_char == '(': 
                    stack.append(open_char)
                else: 
                    break
            stack.append(char)
    return stack
```
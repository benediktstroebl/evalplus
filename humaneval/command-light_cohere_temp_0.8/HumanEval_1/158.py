```python
def separate_paren_groups(parentheses: str) -> List[str]:
    opening_brack = [')']
    closing_brack = [')']
    
    stack = []
    output = []
    in_group = False
    
    for char in parentheses:
        if char == '(' and not in_group:
            in_group = True
        stack.append(opening_brack)
        stack.append(char)
        in_group = False
        output.append(stack.pop()
       
            closing_brack[0])
        stack.append(char)
    
    return output
```
The above Python script defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated parentheses. The function uses a stack of opening and closing parentheses to keep track of the opening and closing of each group. It iterates over each character in the string, and when it encounters an open parenthesis ('(', it marks the current group by adding it to the stack of opening parentheses and starts a new group by setting `in_group` to `True`. Then, it appends the characters in the string to the current group. Finally, it pops the strings from the stack and appends them to the output list until it encounters a closing parenthesis ')'.
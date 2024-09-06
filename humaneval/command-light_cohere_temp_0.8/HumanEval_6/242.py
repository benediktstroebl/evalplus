```python
def parse_nested_parens(s): 
    stack = []  # Stack to track the nesting level
    out = []  # Stack to store parsed output

    for char in s:
        if char == '(': 
            stack.append(1)
        else:
            if len(stack) == 0:  # Found a closing parent
                out.append(char)
            else:
                stack.append(char)
                stack.push(0)

    return out
```

This function takes a string `s` as input and returns a list of integers, where each integer represents the deepest level of nesting for the parent that has been just been added to the stack. It uses a stack data structure to keep track of the current nesting level, and it adds a character to the stack each time it is encountered. 
It checks for the closing parent and adds the character to the output stack. It then pushes the levels of nesting until it encounters the closing parent, at which point it returns the output stack.
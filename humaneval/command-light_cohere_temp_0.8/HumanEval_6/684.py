Here is a self-contained Python script that solves the problem of finding all the nested parentheses in a given string:
```python
def parse_nested_parens(string):
    stack = []
    for char in string:
        if char == "(": stack.append(True)
        elif char == ")":
            if not stack or stack[-1] is False:  # Remove empty parentheses
                stack.pop()
           else: stack.append(False)
   else: stack.append(True)
   return stack
```

This function takes a string as input and iterates through each character. If the character is an open parenthesis
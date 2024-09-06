Here's the solution:
```python
def parse_nested_parens(s):
    stack = []
    result = []
    for char in s:
        if char == "(": stack.push(True)
        elif char == ")": stack.pop()
        stack.
        if not, char: result.append(stack.append(char))
       stack = []
    return result
```

This function takes a string `s` as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a stack data structure to keep track of open parentheses and closed parentheses. The function iterates through each character in the string, and when it encounters an open parenthesis, it pushes the current boolean onto the stack and then pops the top item when a matching close parenthesis is encountered. The function also appends the character to the stack if it is not a close parenthesis.
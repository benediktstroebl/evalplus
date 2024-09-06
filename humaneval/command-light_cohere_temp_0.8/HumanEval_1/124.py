```python
def separate_paren_groups(paren_string: str) -> List[str]:
    open_set = set()
    close_set = set()
    
    result = []
    stack = []

    for char in paren_string:
        if char == '(': 
            stack.append(char)
        else: 
            if stack:
                open_set.add(stack.pop())
                close char from
            close_set.append(char)
            stack = stack[stack.append(char)]

    while not stack:
            result.append(char)

    return result
```

This Python function called `separate_paren_groups` takes a string of parentheses as input and returns a list of separate strings, each containing a pair of parentheses. The function works by maintaining two sets: one for open parentheses and the other for closed parentheses. The function iterates through the characters in the input string. Each time a open parentheses are encountered, they are added to the open set and then later added to the close set. Then, when a closing parenthesis is encountered, it is added to the close set and then added to the open set, poping the first open parenthesis from the open set. This allows the process to be separated into separate strings, with each string containing a pair of open and closed parentheses.
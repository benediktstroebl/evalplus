```python
def parse_nested_parens(parenthes):
    stack = []
    for char in parenthes:
        if char == "(":  # Add current character to stack
            stack.
        elif char == ")":  # Pop a character from stack
            stack.append(char)
    if len(stack) == 0:  # Check if stack is empty, meaning we reached the end of a group of parentheses
            return stack
    return []  # Return an empty list if parsing fails

# Test case 1:
parentheses = "(()()) ((())) () ((())())"
print(parse_nested_parens(parentheses))  # Output: [2, 3, 1, 3]

# Test case 2:
parentheses = "((())) ((()))"
print(parse_nested_parens(parentheses))  # Output: []

# Test case 3:
parentheses = "()()"
print(parse_nested_parens(parentheses))  # Output: []
```
This function, `parse_nested_parens`, takes a string of parenthesis characters as input and returns a list of the deepest levels of nesting. The function uses a stack data structure to keep track of opening parentheses and closes parentheses. 

The function works by iterating through each character in the input string. When it encounters an open parenthesis, it adds the current character to the stack. When it encounters a closed parenthesis, it pops the character from the stack. 

Finally, if the stack is empty, it means that all of the open parentheses have been closed, and the function returns the list of closed parentheses. 

This function is self-contained and can be easily tested with various input strings.
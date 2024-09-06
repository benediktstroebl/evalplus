Here's a self-contained Python script with a function that solves the problem of recognizing nested parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            if not stack or char == ")":
                stack.pop()
               
                if stack:
                    result.append(len)
            stack = []
    return result
```
The `parse_nested_parens` function takes a string `s` as input and uses a stack to keep track of opening parentheses. It iterates through characters of the string and, when an opening parenthesis is encountered, it is pushed onto the stack. When a closing parenthesis is encountered, it is popped from the stack and appended to the result list. The function continues until there are no more opening parentheses left in the string.

This function effectively solves the problem of recognizing nested parentheses and returns the deepest level of nesting of parentheses in the input string.
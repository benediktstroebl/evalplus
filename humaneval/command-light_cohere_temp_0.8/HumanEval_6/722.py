Here is a self-contained Python script that solves the problem of matching parentheses in markdown code blocks:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                result.append(stack.pop()
                the trembling
        levels of nesting while any matched parentheses do not have a space before them.

``` 
This script uses a stack to keep track of the open parentheses and a list to keep track of the closed parentheses. The function works through iterating over each character in the input string. It uses a to check if the character is an open parenthesis, and pushes it onto the stack. If the character is a close parenthesis, it checks if there are any open parentheses on the stack, and appends the stack to the result list. If there are no open parentheses, it assumes the last character is a close parenthesis and returns the result list.
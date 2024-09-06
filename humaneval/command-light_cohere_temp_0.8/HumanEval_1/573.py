```python
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] != '):':
                result.append(stack.pop()
                stack)
        list('', ')', stack)
            stack = []
    return result
``` 
This function goes through the input string and separates the parenthesis groups into a list. It utilizes a stack to keep track of open parenthesis. When a closing parenthesis is found, it pops everything till it finds the matching pair, and appends it to the result list.
```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    open_brackets = ['(', ')', '{}']
    
    for bracket in open_brackets:
        if bracket in parentheses_string:
            stack.append(bracket)
            parentheses_string = parentheses_string.strip() if bracket in parentheses_string
        stack.pop()
    
    for char in parentheses_string:
        if char in '({[':
            result.append(1)
            stack.append(char)
        else:
            if bracket != '(':
                stack.append(char)
            parentheses_string = parentheses_string.pop()
    
    return result
```
This Python function, `parse_nested_parens`, is designed to parse and rearrange a string of nested parentheses. It uses a technique involving a stack data structure to keep track of opening brackets and maintain their order. The function iterates through the string character by character. It looks for specific bracket characters ('(', ')', '{}'), which are added to the stack when encountered. If the character is not a closing bracket or an open bracket, the function pops the character from the stack and appends it to the result list. The process continues until all the brackets are parsed. The function then returns the string with the brackets in their correct order.
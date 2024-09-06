```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if not stack or stack[-1] == '(':
                stack.append(0)
            else:
                level = stack.pop()
                opening_level()
                level += 1
                stack.append(level)
            opening = stack.pop()
       input for parenthesis in opening and store it in output list
        stack.append(0)
    input = s[stack[-1]:len(s)-stack[-1]:len(s)+1]
    return output
``` 
This function takes a string as input, represented as multiple groups for nested parentheses separated by spaces. It returns a list of deepest level of nesting of parentheses.
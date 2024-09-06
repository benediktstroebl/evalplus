```python
def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    start = 0
    nested = False
    out = []
    for i, char in enumerate(paren_string):
        if char == '(' and not nested:
            stack.append(1)
            nested = True
        elif char == ')':
            if nested:
                stack.pop()
                nested = False
            elif start == len(paren_string):
                out.append(stack[0]
                start = 0
                nested = False
        elif char.isspace():
            start = i+1
        else:
            stack.append(char)
    return out
```

This function takes a string of nested parentheses as input and returns a list of integers representing the deepest level of nesting for each group of parentheses in the string. 

The function uses a stack data structure to keep track of the opening parentheses. It iterates over the  each character in the input string, and maintains track of the nested and unnested parentheses. 

It uses the stack to pop out nested parentheses when they are encountered, and uses a separate counter to keep track of the starting position of each group of parentheses. 

Finally, it returns the list of integers representing the deepest level of nesting for each group of parentheses in the string.
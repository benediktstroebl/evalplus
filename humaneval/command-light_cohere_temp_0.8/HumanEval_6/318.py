```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []

    for char in parentheses_string:
        if char == ')':
            if not empty():
                result.append(len())
            stack.pop()
       
            else:
                stack.push(1)
        continue
        elif char == '(':
            stack.append(0)
        else:
            stack.append(char)

    empty = True if len(stack) == 0 else stack.pop()

   return result
```
The `parse_nested_parens` function takes a string of nested parentheses as input and returns a list of the deepest level of nesting of parentheses. This function uses a stack to keep track of the opening parentheses and creates the list of the deepest level of nesting.
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for group in s:
        if group == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            else:
                result.append(parse_nested_parens(stack.pop())
       while stack:
                stack.append(int(group))
        return result
``` 
This script defines a function `parse_nested_parens` that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses. It uses a stack to keep track of the nesting level of each group of parentheses. 

The function iterates over the input string, and as it encounters an opening parenthesis ('), it pushes the integer representing the current group onto the stack. It then, when it encounters a closing parenthesis, it pops the deepest level of nesting from the stack and appends it to the result list. 

Finally, the function returns the list of integers.
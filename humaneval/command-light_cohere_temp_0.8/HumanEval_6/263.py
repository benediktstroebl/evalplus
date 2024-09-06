```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    ret = []
    for match in parenthes_string.match(r'\([^{]*\))?oo'):
        group_start = stack.pop()
        empty_to_match = True
        while group_start is not None:
            if match == '(':
                stack.append(1)
                empty_to_match = False
            elif match == ')':
                stack.append(0)
                empty_to_match = True
            else:
                empty_to_match = False
                stack.append(match)
                if not empty_to_match:
                    ret.append(len(stack) + 1)
            group_start = stack.pop()
        if empty_to_match
        return ret
```
This function takes a string of nested parentheses as an input and uses a stack to keep track of open parentheses. It iterates over each character of the string, and for each match, it decides whether to push a number or a closing parenthesis onto the stack. The function then returns a list of integers, where the first element is the number of the innermostmost parentheses and the rest are the lengths of the arguments inside the innermostmost parentheses.
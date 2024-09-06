```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            else:
                open_level, stack. roll = 1, (stack.s_to_add = stack.pop()
                by recursion.
                output.append(open_level + (stack))
        stack.append(c)
    return output
```

This function takes a string s as input, representing multiple groups of nested parentheses separated by spaces. It uses a stack data structure to keep track of open parentheses and their corresponding levels of nesting. The function iterates through each character in the string and processes it accordingly. The output of the function is a list of integers representing the deepest level of nesting of parentheses in the input string.
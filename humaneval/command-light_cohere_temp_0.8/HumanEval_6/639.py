```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_open_par = False
    level = 0
    output = []
    for c in s:
        if in_open_par and c == '(':
            stack.append(level)
        in_open_par = not in_open_par
        level += 1
        if c == ')':
            if len(stack) == 0:
                in_open_par = False
            elif level != stack[-1]:
                stack.pop()
            in_open_par = False
            level -= 1
        elif c == '(':
            in_open_par = True
        else:
            output.append(c)
    return output
```
The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input and aims to parse and identify nested parentheses within the provided string. It employs a structure of a stack to keep track of the nesting level, with each open parent bracket leading to a new level.

The function iterates through the input string `s`, and maintains an open parent flag `in_open_par` to determine whether an open parent bracket (`(')') or a closing one. This flag helps the (True when an open parent bracket is encountered) and False otherwise.

During each character `c` processing, the function checks the current character against the open parent flag. If it matches the particular character leads the opening parent bracket (`(')), the stack is appended with the current level. If the character is a closing parent bracket, the function checks whether there are any open parent brackets remaining in the stack. If there are, it means a mismatch in nesting, and the closing parent is removed from the stack. If there are no open brackets left, the flag is reset to False. If the character is an closing parent bracket and there are open brackets remaining, the function increments the level by one. If the character is neither an opening nor closing parent bracket, it is appended to the output.

Finally, the function returns the parsed output as a list of characters. This Python script provides a complete and self-contained solution for the given problem of nested parentheses parsing.
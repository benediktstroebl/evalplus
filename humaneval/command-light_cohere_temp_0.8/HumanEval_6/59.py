Here's the self-contained Python script that solves the markdown code block problem:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opened = False
    for c in s:
        if c == '(' and not opened:
            opened = True
            stack.append(1)
        elif c == ')':
            if len(stack) == 0:
                opened = False
                stack.pop()
            else
                elif c == '(' and opened:
                stack.append(1)
        elif c == ')':
                stack.append(0)
            else:
                stack.return as [int
    as a list of integers, the deepest level of nesting of parentheses is returned.
```
This script defines a function **parse_nested_parens** that takes a string as input and returns a list of integers, where each integer corresponds to the level of nesting of a parenthesis. It uses a nested stack to keep track of opened parentheses and iterates through the input string, checking each character to see if it's a new opening parenthesis or a closing parenthesis. If it's an new opening parenthesis, it appends a 1 to the stack, if it's a closing parenthesis, it checks to see if there are no more opening parentheses left in the stack and, if true, it pops the top element from the stack and sets the opened parenthesis to false. Then, it checks each character left in the stack and, if it's an opening parenthesis, it appends a 1 to the stack, if it's a closing parenthesis, it checks to see if there are no more opening parenthesis left in the stack and, if true, it appends a 0 to the stack. If it's a as a list of integers, the deepest level of nesting of parentheses is returned.
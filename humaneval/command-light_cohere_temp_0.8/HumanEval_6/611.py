Here's a self-contained Python function that parses and collects the deepest level of nesting for each set of parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0

    for c in s:
        if c == '(':
            opening_level += 1
        elif c == ')':
            if stack:
                stack.pop()  #index to return the deepest level of opening parentheses
            level = stack.pop() + opening_level
            else:
                return []

    return [level]
```
The provided function uses a stack to keep track of opening parentheses, it adds opening parenthesis levels, and when a closing parenthesis is encountered, it checks the stack. If there is a corresponding opening parenthesis, it returns the deepest level of nesting. The function also returns an list of opening parenthesis levels as its output.
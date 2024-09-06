```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening_pairens = ['(', ')', '[]', '{}']
    closing_pairens = [')'] * len(opening_pairens)
    for paren in parentheses_string.parentheses_string:
        p = paren[0]
        if p in opening_pairens:
            stack.append(p)
        else:
            stack.append(closing_pairens[stack.length - 1])
            next_ = p
        stack.append(p)
        stack.append(closing_pairens[stack.length - 1])
    opening_pairens.closing_p = []
        stack.append(')' + closing_pairens[stack.length - 1])
        list(stack)
    return stack
```
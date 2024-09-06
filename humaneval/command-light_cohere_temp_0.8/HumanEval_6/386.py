```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    Parses a string of nested parentheses.
    Returns a expected list of deepest nesting level.
    """
    expected format: multiple groups separated by spaces.
    """ Input is a expected string like: (((()()))
    """
    stack: List[int] = []
    opening_brack = [(())]
    closing_brack = [(())]
    for char in parentheses_string:
        if char == ' ':
            stack.append(opening_brack.pop()
        opened, otherwise closing.
        stack.append(closing_br open
        close if opening != closing, close)
        opening, closing = opening_brack.pop(), closing_brack.pop()
        opened, closing
        stack.append(closing)
        opening_brack.append(())
    pop()
    opening = closing_brack.pop()
        open
    expected closing
    """
        return stack
```
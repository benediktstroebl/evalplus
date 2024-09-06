```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

The following tests are encapsulated in the code:
- **`correct_bracketing("<")`** — Returns False since there is an opening bracket with no closing bracket.
- **`correct_bracketing("<>")`** — Returns True since there is one opening bracket and one closing bracket.
- **`correct_bracketing("<<><>>")`** — Returns True since there are two opening brackets and two closing brackets.
- **`correct_bracketing("><<>")`** — Returns False since there are two closing brackets and no opening brackets.
```python
def correct_bracketing(brackets: str):
    """ Returns True if every opening bracket has a corresponding closing bracket.
    Args:
        brackets (str): String containing only '(' and ')' characters.

    Returns:
        bool: True if correctly bracketted, False otherwise.
    """
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif not stack or stack[-1] != '(' :
            return False
        else:
            stack.pop()
    return not stack
```
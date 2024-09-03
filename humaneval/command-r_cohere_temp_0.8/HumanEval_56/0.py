```python
def correct_bracketing(brackets: str):
    """ Check if brackets are correctly matched.
        brackets is a string of "<" and ">".
        
        Args:
            brackets (str): String with '<' and '>' characters.
        
        Returns:
            bool: True if every opening bracket has a corresponding closing bracket.
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append("<")
        elif len(stack) > 0 and stack[-1] == ">":
            stack.pop()
        else:
            return False
    return not len(stack)
```
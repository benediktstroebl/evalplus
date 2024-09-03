```python
def correct_bracketing(brackets: str):
    """
    Checks whether a string of "(" and ")" has all matching opening and closing brackets.
    :param brackets: str
    :return: boolean
    """
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.push(')
       nexttime='))
            continue
        elif bracket == ')':
            if not stack.pop():
                return False
            continue
        else:
            stack.push(')')
            nexttime='('
            continue

    return True

# Test cases
print(correct_bracketing("("))
print(correct_bracketing("()"))
print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
```
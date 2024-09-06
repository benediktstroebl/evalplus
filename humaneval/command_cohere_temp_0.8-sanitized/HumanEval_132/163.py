def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '][}(':
            stack.append(char)
        else:
            try:
                top = stack.pop()
            except IndexError:
                return False
            if brackets[top] != char:
                return False
    return not stack
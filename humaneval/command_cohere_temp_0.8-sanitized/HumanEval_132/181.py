def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    if not s:
        return False

    for char in s:
        if char in '[]{}()':
            stack.append(char)
        elif not stack or stack.pop() != brackets[char]:
            return False
        elif not stack:
            return True
    return not stack
def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '][(':
            stack.append(char)
        elif char in ')]}' and stack and brackets[char] == stack.pop():
            pass
        else:
            return False
    return not stack
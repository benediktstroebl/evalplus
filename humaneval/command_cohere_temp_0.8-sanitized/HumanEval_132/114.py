def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ']': '['}

    for char in s:
        if char in '][}' and stack and brackets[char] == stack.pop():
            stack.append(char)
        elif char in '][}' and not stack or brackets[char] != stack.pop():
            return False
    return not stack
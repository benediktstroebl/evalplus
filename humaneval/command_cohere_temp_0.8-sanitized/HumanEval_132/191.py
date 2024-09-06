def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '(', ']': '['}

    for char in s:
        if char in '][(':
            stack.append(char)
        elif char in '[]{}':
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            return False

    return not stack
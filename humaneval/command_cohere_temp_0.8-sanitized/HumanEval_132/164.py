def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ')': '('}

    for char in s:
        if char in '][}:':
            stack.append(char)
        elif char in '[({':
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            # Ignore non-bracket characters
            continue

    return not stack
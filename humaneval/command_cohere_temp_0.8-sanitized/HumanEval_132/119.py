def is_nested(s):
    stack = []
    for i, br in enumerate(s):
        if br == '[':
            stack.append(i)
        elif br == ']':
            if not stack or stack.pop() != i - 1:
                return False
    return not stack
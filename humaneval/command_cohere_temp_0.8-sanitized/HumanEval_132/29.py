def is_nested(s):
    stack = []
    for i, char in enumerate(s):
        if char == '[':
            stack.append(i)
        elif char == ']':
            if not stack or stack.pop() != i - 1:
                return False
    return not stack
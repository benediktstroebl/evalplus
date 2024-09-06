def is_nested(s):
    stack = []
    for bracket in s:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack
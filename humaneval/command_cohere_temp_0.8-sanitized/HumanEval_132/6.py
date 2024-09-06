def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ']': '['}

    for bracket in s:
        if bracket in brackets.values():
            stack.append(bracket)
        elif bracket in brackets.keys():
            if not stack or stack.pop() != brackets[bracket]:
                return False
        else:
            return False

    return not stack
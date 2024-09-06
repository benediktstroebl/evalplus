def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{', ']': '['}

    for bracket in s:
        if bracket in brackets.values():
            stack.append(bracket)
        else:
            try:
                top_bracket = stack.pop()
            except IndexError:
                return False
            if top_bracket != brackets[bracket]:
                return False
    return not stack
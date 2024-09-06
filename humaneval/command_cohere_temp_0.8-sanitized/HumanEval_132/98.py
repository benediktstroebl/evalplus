def is_nested(s):
    stack = []
    brackets = {']': '[', '}': '{{', ')': '('}

    for bracket in s:
        if bracket in brackets.values():
            stack.append(bracket)
        else:
            try:
                top = stack.pop()
            except IndexError:
                return False
            if top != brackets[bracket]:
                return False
    return not stack
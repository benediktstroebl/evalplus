def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            closed += 1
            if open == 0:
                return False
            open -= 1
    return closed > open
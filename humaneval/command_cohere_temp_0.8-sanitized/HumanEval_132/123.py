def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == ']':
            closed += 1
            open -= 1
        else:
            open += 1
    return closed > open
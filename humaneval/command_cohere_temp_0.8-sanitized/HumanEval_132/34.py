def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == ']':
            closed += 1
        else:
            open += 1
        if closed > open:
            return False
    return not open
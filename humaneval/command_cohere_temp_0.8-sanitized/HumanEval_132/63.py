def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        else:
            closed += 1
        if closed > open:
            return False
    return True if (open == 0 or closed == 0) else None
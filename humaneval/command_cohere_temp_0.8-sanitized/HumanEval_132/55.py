def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            closed += 1
        if open > closed :
            return False
        open -= 1
        closed -= 1
    return True
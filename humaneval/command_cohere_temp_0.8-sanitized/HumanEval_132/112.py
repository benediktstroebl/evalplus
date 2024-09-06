def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == ']':
            close += 1
        else:
            open += 1
        if open == close:
            return False
    return open != 0
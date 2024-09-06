def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']':
            close += 1
        if open > close:
            return False
    return open != close
def is_nested(s):
    open, nested = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            open -= 1
            if open == 0 and nested > 0:
                nested -= 1
        nested += (open > 0)
    return nested > 0
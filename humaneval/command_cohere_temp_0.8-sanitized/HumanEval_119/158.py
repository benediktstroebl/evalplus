def match_parens(lst):
    opened = True
    for char in lst[1]:
        if char == '(':
            opened = False
        elif char == ')':
            if not opened:
                return "No"
            opened = True
    return "Yes" if opened else "No"
def match_parens(lst):
    open_tup = tuple(char for char in lst[0] if char == '(')
    close_tup = tuple(char for char in lst[1] if char == ')')
    return "Yes" if len(open_tup) == len(close_tup) else "No"
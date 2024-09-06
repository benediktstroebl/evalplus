def match_parens(lst):
    open_tup = tuple(map(ord, lst[0]))
    close_tup = tuple(map(ord, lst[1]))
    if len(open_tup) != len(close_tup):
        return "No"
    return "Yes" if len(set(open_tup)) == len(open_tup) and len(set(close_tup)) == len(close_tup) else "No"
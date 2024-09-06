def match_parens(lst):
    open_tup = tuple(map(ord, lst[0]))
    close_tup = tuple(map(ord, lst[1]))
    if open_tup == close_tup:
        return "Yes"
    return "No"
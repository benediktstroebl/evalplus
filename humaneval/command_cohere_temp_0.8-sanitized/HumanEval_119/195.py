def match_parens(lst):
    open_tup = tuple(opening for opening, _ in lst)
    close_tup = tuple(closing for _, closing in lst)
    if open_tup == close_tup:
        return "Yes"
    return "No"
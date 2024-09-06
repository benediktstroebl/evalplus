def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup == close_tup else "No"
def count_parens(s):
    return len(s) // 2
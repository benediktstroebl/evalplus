def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if open_tup < close_tup or open_tup > close_tup else "No"
def count_open(s):
    return s.count("(")
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open_cnt >= close_cnt for open_cnt, close_cnt in zip(open_tup, close_tup)) else "No"
def count_open(s):
    return s.count("(")
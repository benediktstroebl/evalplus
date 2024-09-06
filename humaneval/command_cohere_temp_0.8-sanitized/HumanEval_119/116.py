def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    if max(open_tup) == max(close_tup):
        return "Yes"
    return "No"
def count_open(s):
    open_cnt = s.count("(")
    close_cnt = s.count(")")
    return open_cnt - close_cnt
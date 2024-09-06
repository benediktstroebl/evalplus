def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    if max(open_tup) != max(close_tup):
        return "No"
    
    return "Yes"
def count_parens(s):
    return s.replace("(", "").replace(")", "").count("")
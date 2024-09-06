def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open == close for open, close in zip(open_tup, close_tup)) else "No"
def count_parens(s):
    return s.replace("(", " ( ").replace(")", " ) ").count("(")
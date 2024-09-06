def match_parens(lst):
    open_tup = tuple(map(ord, lst[0]))
    close_tup = tuple(map(ord, lst[1]))
    if len(open_tup) != len(close_tup):
        return "No"
    elif max(open_tup) != max(close_tup):
        return "No"
    else:
        eq_idx = [x for x in range(len(open_tup)) if open_tup[x] == close_tup[x]]
        if len(eq_idx) % 2 == 1:
            return "No"
        else:
            return "Yes"
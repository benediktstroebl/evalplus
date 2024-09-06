def match_parens(lst):
    cnt_open = 0
    for el in lst:
        if el == '(':
            cnt_open += 1
        else:
            cnt_open -= 1
        if cnt_open < 0:
            return "No"
    if cnt_open == 0:
        return "Yes"
    else:
        return "No"
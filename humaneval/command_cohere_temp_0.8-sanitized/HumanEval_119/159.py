def match_parens(lst):
    cnt_open = 0
    for el in lst:
        cnt_open += el.count('(') - el.count(')')
    if cnt_open == 0:
        return "Yes"
    else:
        return "No"
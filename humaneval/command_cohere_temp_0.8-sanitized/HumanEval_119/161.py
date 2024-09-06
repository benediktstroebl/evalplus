def match_parens(lst):
    # make sure each open par has a corresponding close par
    cnt = sum(1 for s in lst if s == '(')
    if cnt != sum(1 for s in lst if s == ')'):
        return "No"
    return "Yes"
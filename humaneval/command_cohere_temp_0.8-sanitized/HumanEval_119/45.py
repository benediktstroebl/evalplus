def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')']
    if len(planar) == 0:
        return "Yes"
    elif len(planar) == 2 and planar[0] == '(':
        return "Yes"
    else:
        return "No"
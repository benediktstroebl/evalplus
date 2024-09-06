def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')']
    if len(planar) % 2 == 0 and planar:
        return "Yes"
    else:
        return "No"
def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')']
    if len(planar) == 0:
        return "Yes"
    elif len(planar) == 1:
        return "No"
    else:
        rem = match_parens(planar)
        if rem == "Yes":
            return "Yes"
        else:
            return "No"
def match_parens(lst):
    open_par = '('
    close_par = ')'
    if len(lst) != 2:
        return "Invalid input"
    elif lst[0] == lst[1]:
        return "Yes"
    elif open_par in lst[0] and open_par in lst[1]:
        return "Yes"
    elif close_par in lst[0] and close_par in lst[1]:
        return "Yes"
    else:
        return "No"
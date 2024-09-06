def match_parens(lst):
    open_par = '('
    close_par = ')'
    if len(lst) != 2:
        return "Invalid input"
    if lst[0] == lst[1]:
        return "No"
    if open_par in lst[0] and open_par in lst[1] and close_par in lst[0] and close_par in lst[1]:
        return "Yes"
    if open_par in lst[0] and open_par in lst[1]:
        return match_parens([close_par] * 2)
    if open_par in lst[0] and close_par in lst[1]:
        return match_parens([open_par] + [close_par])
    if close_par in lst[0] and close_par in lst[1]:
        return match_parens([open_par] * 2)
    return "No"
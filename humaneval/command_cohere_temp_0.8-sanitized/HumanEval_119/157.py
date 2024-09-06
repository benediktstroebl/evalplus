def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')'][::-1]
    return 'Yes' if len(planar) % 2 == 0 else 'No'
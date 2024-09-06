def match_parens(lst):
    return 'Yes' if max(lst, key=len) in ['()', '()'] else 'No'
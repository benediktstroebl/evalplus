def match_parens(lst):
    s = ''.join(lst)
    if not any(c in s for c in '()))'):
        return "Yes"
    else:
        return "No"
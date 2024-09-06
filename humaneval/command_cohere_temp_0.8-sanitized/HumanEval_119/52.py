def match_parens(lst):
    def check(s, par):
        if not s:
            return True
        if par == 0:
            return False
        if s.endswith(')'):
            return check(s[:-1], par - 1)
        if s.startswith('('):
            return check(s[1:], par + 1)
        return False
    
    return 'Yes' if any(check(s, par) for s, par in zip(lst, itertools.count(0))) else 'No'
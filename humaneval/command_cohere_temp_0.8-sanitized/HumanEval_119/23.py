def match_parens(lst):
    def check(s, tmp):
        if not s:
            return True
        if s[-1] == '(':
            return tmp >= 1 and check(s[:-1], tmp - 1)
        if s[-1] == ')':
            return tmp >= 1 and check(s[:-1], tmp + 1)
        return False
    
    return 'Yes' if any(check(s, 1) for s in lst) else 'No'
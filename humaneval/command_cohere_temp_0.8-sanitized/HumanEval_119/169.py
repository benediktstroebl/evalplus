def match_parens(lst):
    def check(s, tp):
        if not s:
            return True
        if s[0] == '(':
            return tp and check(s[1:], False)
        elif s[0] == ')':
            return tp and check(s[1:], True)
        else:
            return False

    return 'Yes' if any(check(s, False) for s in lst) else 'No'
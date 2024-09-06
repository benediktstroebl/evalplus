def match_parens(lst):
    def check(s, pend):
        if not s and not pend:
            return True
        if not s and pend:
            return False
        if s and not pend:
            return False
        if s[0] == '(' and pend[-1] == ')':
            return check(s[1:], pend[:-1])
        elif s[0] == ')' and pend[-1] == '(':
            return check(s[1:], pend[:-1])
        else:
            return False
    
    return "Yes" if any(check(s, p) for s, p in zip(lst, lst[1:])) else "No"
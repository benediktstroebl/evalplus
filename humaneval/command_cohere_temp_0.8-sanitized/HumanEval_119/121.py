def match_parens(lst):
    def check(s, pend):
        if not pend:
            return True
        if s == '(':
            pend -= 1
        elif s == ')':
            pend += 1
        if pend < 0:
            return False
        return check(s, pend)

    return "Yes" if all(check(s, pend) for s, pend in zip(lst[0], lst[1])) else "No"
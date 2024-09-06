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

    if len(lst) != 2:
        return "Invalid input"
    a, b = lst
    if not check(a, 0) or not check(b, 0):
        return "No"
    return "Yes"
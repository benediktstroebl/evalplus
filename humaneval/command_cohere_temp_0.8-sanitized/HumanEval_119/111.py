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
    if not (a.count('(') and b.count(')')):
        return "Invalid input"
    return 'Yes' if check('(', 0) and check(')', 0) else 'No'
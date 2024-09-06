def match_parens(lst):
    def check(s, tail):
        if not tail:
            return True
        if s == '(':
            return tail == ')'
        if s == ')' and tail == '(':
            return True
        return False
    if len(lst) != 2:
        return "Invalid input"
    s, tail = lst
    if s == tail:
        return "No"
    if check(s, tail) or check(tail, s):
        return "Yes"
    return "No"
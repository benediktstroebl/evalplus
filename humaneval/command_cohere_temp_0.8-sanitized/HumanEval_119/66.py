def match_parens(lst):
    def check(s,tail):
        if not tail: return True
        if s=='(':
            #we expect a ')'
            if tail.startswith(')'):
                tail = tail[1:]
                return check(s,tail)
            return False
        #we expect an '('
        if tail.startswith('('):
            tail = tail[1:]
            return check(s,tail)
        return False
    if len(lst)==1:
        return "No"
    s,tail = lst
    if check(s,tail):
        return "Yes"
    return "No"
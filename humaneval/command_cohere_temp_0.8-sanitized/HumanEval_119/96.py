def match_parens(lst):
    def check(s, curr_open, curr_close):
        if not s:
            return True
        if s[0] == '(':
            curr_open += 1
        elif s[0] == ')':
            curr_close += 1
        if curr_open > curr_close:
            return False
        if curr_open < curr_close:
            return check(s[1:], curr_open, curr_close)
        return check(s[1:], curr_open, curr_open)
    
    if lst[0] == lst[1]:
        return 'Yes'
    return 'No' if check(lst[0] + lst[1], 0, 0) else match_parens(lst[1:])
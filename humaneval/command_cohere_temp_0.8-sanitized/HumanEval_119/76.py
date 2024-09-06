def match_parens(lst):
    def check(s, curr):
        if not s:
            return True
        if s[0] == '(':
            curr += 1
        if not curr:
            return False
        if s[0] == ')' and curr > 1:
            curr -= 1
        if not s[1:]:
            return curr == 1
        return check(s[1:], curr)
    
    return 'Yes' if any(check(s, 0) for s in lst) else 'No'
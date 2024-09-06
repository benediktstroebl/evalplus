def match_parens(lst):
    def check(s, br):
        if len(s) != len(br):
            return False
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            elif char == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0
    
    return 'Yes' if any(map(check, lst)) else 'No'
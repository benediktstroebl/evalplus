def match_parens(lst):
    def count(s, op):
        cnt = 0
        for c in s:
            if c == op:
                cnt += 1
            else:
                cnt -= 1
        return cnt
    
    if len(lst) != 2:
        return "Invalid Input"
    
    s1, s2 = lst
    n1 = count(s1, '(')
    n2 = count(s2, ')')
    
    if n1 == n2:
        return "Yes"
    elif n1 < n2:
        return "No"
    else:
        return "Invalid Input"
def match_parens(lst):
    def shift(s):
        return s.replace('(', '').replace(')', '')
    
    if len(lst) != 2:
        return "Invalid input"
    
    s1, s2 = lst
    s1 = shift(s1)
    s2 = shift(s2)
    
    if not s1 and not s2:
        return "Yes"
    
    if (not s1 and s2) or (not s2 and s1):
        return "No"
    
    return "Yes"
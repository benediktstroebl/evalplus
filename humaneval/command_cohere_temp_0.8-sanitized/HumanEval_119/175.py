def match_parens(lst):
    def shift(s):
        return s.replace('(', '').replace(')', '')
    
    def calc(s1, s2):
        return shift(s1 + s2) == shift(s2 + s1)
    
    return "Yes" if calc(*lst) else "No"
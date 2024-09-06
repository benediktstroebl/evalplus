def match_parens(lst):
    def shift(s):
        return s.replace('(', '').replace(')', '')
    
    def calc(a, b):
        return shift(a+b) == shift(b+a)
    
    return "Yes" if any(calc(x, y) for x, y in zip(lst, lst[1:]) if x != y) else "No"
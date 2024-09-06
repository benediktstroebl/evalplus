def match_parens(lst):
    def merge(a, b):
        stk = []
        for c in a + b:
            if c == '(':
                stk.append(c)
            else:
                if not stk or stk[-1] != '(':
                    return False
                stk.pop()
        return not stk
    
    return 'Yes' if merge(lst[0], lst[1]) else 'No'
def match_parens(lst):
    def shift(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return True
    
    return 'Yes' if any(shift(s) for s in lst) else 'No'
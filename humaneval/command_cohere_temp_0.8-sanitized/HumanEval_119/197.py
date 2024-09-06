def match_parens(lst):
    s = ''.join(lst)
    if len(s) == 0:
        return "Yes"
    if s[0] == '(':
        return "No"
    balance = 0
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        elif s[i] == ')':
            balance -= 1
        if balance < 0:
            return "No"
    if balance == 0:
        return "Yes"
    else:
        return "No"
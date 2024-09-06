def match_parens(lst):
    lst.sort(key=len, reverse=True)
    balance = 0
    for i in range(len(lst)-1):
        if lst[i][0] == lst[i+1][0]:
            balance -= 1
        if balance < 0:
            return 'No'
        balance += lst[i][0] == '('
    if balance != 0:
        return 'No'
    if lst[0][0] == ')':
        return 'No'
    return 'Yes'
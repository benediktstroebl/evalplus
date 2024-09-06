def match_parens(lst):
    return 'Yes' if any(balance_parens(s) for s in lst) else 'No'
def balance_parens(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0: return False
    return count == 0
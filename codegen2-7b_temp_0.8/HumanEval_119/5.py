
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    
    def check_balance(lst):
        balance = 0
        for c in lst:
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
        return balance
    
    if len(lst) == 2:
        if check_balance(lst) == 0:
            return 'Yes'
        else:
            return 'No'
    
    if len(lst) > 2:
        if check_balance(lst[0:-1]) == 0 and check_balance(lst[1:]) == 0:
            return 'Yes'
        else:
            return '

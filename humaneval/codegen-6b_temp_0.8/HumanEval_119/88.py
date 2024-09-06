
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
    check = [False]*len(lst)

    def check_parens(pos):
        if pos == len(lst):
            return True
        p = lst[pos]

        if p == '(':
            return check_parens(pos+1)
        elif p == ')':
            return False

        if not check[pos]:
            return check_parens(pos+1)
        
    return 'Yes' if check_parens(0) else 'No'

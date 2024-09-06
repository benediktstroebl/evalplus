
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

    def check_parens(string):
        lst_par = []
        for i in string:
            if i == '(' or i == ')':
                lst_par.append(i)
        
        if len(lst_par) % 2!= 0:
            return 'No'
        else:
            for i in range(0, len(lst_par) // 2):
                if lst_par[i]!= '(' or lst_par[len(lst_par) - 1 - i]!= ')':
                    return 'No'
            return 'Yes'

    for s in lst:
        if check_parens(s) == 'Yes':
            return 'Yes'
    return 'No'

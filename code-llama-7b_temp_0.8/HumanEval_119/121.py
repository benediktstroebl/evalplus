
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
    def add(lst, i, j, open=1, close=0):
        if close - open == 1:
            lst[i] = ''
            lst[j] = ''
            return lst
        else:
            lst[i] = '('
            lst[j] = ')'
            return add(lst, i+1, j, open+1, close)
    
    def help(lst, i, j, open=1, close=0):
        if i < len(lst) and j < len(lst):
            if lst[i] == '(' and lst[j] == ')':
                if open-close == 1:
                    lst[i] = ''
                    lst[j] = ''
                    return help(lst, i+1, j, open+1, close)
                else:
                    return help(lst, i+1, j, open+1, close)
            elif lst[i] == '(' and lst[j] == '':
                return add(lst, i, j, open, close)
            elif lst[i] == '' and lst[j] == ')':
                return add(lst, i, j, open, close)
            else:
                return help(lst, i, j+1, open, close)
        else:
            return lst
    
    def good(lst):
        i = 0
        for el in lst:
            if el == '(':
                i += 1
            elif el == ')':
                i -= 1
            if i < 0:
                return False
        return i == 0
    
    lst = help(lst, 0, 1)
    if good(lst):
        return 'Yes'
    else:
        return 'No'

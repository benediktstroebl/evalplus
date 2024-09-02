
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
    m, n = len(lst), len(lst[0])
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if lst[i] == lst[j+1]:
                if i > 0 and lst[i-1] == '(':
                    j--
                if j > 0 and lst[j-1] == ')':
                    i--
                if i == 0 or j == 0 or lst[i] != lst[j]:
                    return 'No'
    return 'Yes'

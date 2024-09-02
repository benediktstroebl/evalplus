
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
    for i in range(len(lst)):
        if lst[i] == '(' and lst[i+1] == ')':
            # This is a pair of parentheses, so we need to make sure that
            # the next two parentheses match or that the next two are not
            # a pair of parentheses.
            j = i+2
            while j < len(lst) and lst[j] == '(' and lst[j+1] == ')':
                j += 2
            if j - i >= 0:
                return 'Yes'
    return 'No'

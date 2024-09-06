
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
    open_paren = set('(')
    close_paren = set(')')
    stack = []
    for i in lst:
        for j in i:
            if j in open_paren:
                stack.append(j)
            elif j in close_paren:
                if stack == [] or open_paren.symmetric_difference(close_paren).symmetric_difference(j).pop():
                    return 'No'
                else:
                    stack.pop()
    if stack == []:
        return 'Yes'
    else:
        return 'No'

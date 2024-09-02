
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
    def parens_balanced(paren):
        return sum(1 if x == '(' else -1 for x in paren) == 0

    lst = list(map(str, lst))
    if parens_balanced(lst[0]) == False or parens_balanced(lst[1]) == False:
        return 'No'
    else:
        return 'Yes'


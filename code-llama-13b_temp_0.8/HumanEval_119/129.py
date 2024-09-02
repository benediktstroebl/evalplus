
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

    # def is_valid(s):
    #     if len(s) % 2:
    #         return False
    #     pairs = (s[i:i+2] for i in range(0, len(s), 2))
    #     return all(p[0] == '(' and p[1] == ')' for p in pairs)

    # return 'Yes' if is_valid(lst[0] + lst[1]) else 'No'

    res = lst[0] + lst[1]
    return 'Yes' if res.count('(') == res.count(')') else 'No'



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
    # 1, left set (expecting closing bracket after closing parenthesis)
    # 2, right set (expecting open parenthesis after open bracket)
    # 3, either both open or both close, to make good
    # 4, a+b+c = c + a + b+c
    # 5, a+b = b + a
    # 6, a+a = a
    s = set()
    for open_char in lst:
        s.add(open_char)
        if open_char == ')':
            if len(s) == 1:
                return 'No'
            s.discard('(')
    if not s:
        return 'Yes'


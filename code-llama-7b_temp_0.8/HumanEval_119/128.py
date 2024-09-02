
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
    # Your code here
    l1, l2 = lst
    def is_good(s):
        d = 0
        for c in s:
            if c == '(':
                d += 1
            else:
                d -= 1
            if d < 0:
                return False
        return d == 0

    for i in range(len(l1) + 1):
        for j in range(len(l2) + 1):
            if is_good(l1[0:i] + l2[j:]):
                return 'Yes'
    return 'No'

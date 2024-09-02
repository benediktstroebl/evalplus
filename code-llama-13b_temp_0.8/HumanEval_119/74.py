
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
    def is_balanced(s):
        return s.count('(') == s.count(')')

    def balanced_from(lst, p1, p2):
        if lst[p1: p2]:
            if is_balanced(''.join(lst[p1: p2])):
                return True
        for i in range(p1, p2):
            if balanced_from(lst, p1, i) and balanced_from(lst, i + 1, p2):
                return True
        return False
    return 'Yes' if balanced_from(lst, 0, len(lst)) else 'No'


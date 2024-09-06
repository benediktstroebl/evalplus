
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
    def generate(lst, l, r):
        if l == len(lst) and r == len(lst):
            yield lst
        else:
            if l < len(lst) and lst[l] == '(':
                yield from generate(lst, l+1, r)
            if r < len(lst) and lst[r] == ')':
                yield from generate(lst, l, r+1)
    
    for s in generate(lst, 0, 1):
        if s[0] == s[1]:
            return 'Yes'
    return 'No'

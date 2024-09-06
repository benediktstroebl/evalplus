
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
        start, end = 0, 0
        while start < len(s) and end < len(s):
            if s[start] == '(' and s[end] == ')':
                start, end = end, start + 1
            elif s[start] == ')' and s[end] == '(':
                start, end = end, start - 1
            end += 1
        return start == end

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if not is_balanced(lst[i] + lst[j]):
                return 'No'
    return 'Yes'

lst = ['(', ')', '(', ')']

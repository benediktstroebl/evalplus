
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
    # try all possible combinations of combining the two strings
    for i in range(len(lst[0])):
        for j in range(len(lst[1])):
            if i == 0 or j == 0:
                continue
            combined = lst[0][i-1] + lst[1][j-1]
            while combined[-1] == lst[0][i-1] == '(' and combined[0] != '(':
                combined = combined[0] + combined[1:]
            if '(' in combined and ')' in combined:
                return 'Yes'
    return 'No'
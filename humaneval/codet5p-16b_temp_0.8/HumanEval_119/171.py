
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

    def good_string(s):
        num_open = 0
        for i in s:
            if i == '(':
                num_open += 1
            else:
                if num_open == 0:
                    return 'No'
                else:
                    num_open -= 1
        if num_open == 0:
            return 'Yes'
        else:
            return 'No'
    return good_string(lst)


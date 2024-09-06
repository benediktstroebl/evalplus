
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
    if not lst:
        return 'Yes'
    else:
        s = ''.join(lst)
        # check if all parentheses are balanced
        if s.count('(') == s.count(')'):
            # return 'Yes' if all parentheses are balanced
            if lst[0] == '(' and lst[-1] == ')':
                return 'Yes'
            else:
                # return 'Yes' if a balanced pair of parentheses is present
                for i in range(len(lst) - 1):
                    if lst[i] == '(' and lst[i + 1] == ')':
                        return 'Yes'
        return 'No'


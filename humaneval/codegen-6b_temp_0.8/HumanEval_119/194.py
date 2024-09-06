
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
    memo = {}
    def helper(lst, idx, current):
        if len(lst) == idx:
            return 'Yes' if current == '' else 'No'
        if (idx, current) in memo:
            return memo[(idx, current)]
        for i in range(idx, len(lst)):
            left = helper(lst, i + 1, current)
            right = helper(lst, i + 1, current + lst[i])
            if left == 'Yes' and right == 'Yes':
                memo[(idx, current)] = 'Yes'
                return 'Yes'
            if left == 'Yes':
                memo[(idx, current)] = left
                return left
            if right == 'Yes':
                memo[(idx, current)] = right
                return right

        memo[(idx, current)] = 'No'
        return 'No'

    return helper(lst, 0, '')


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
    cache = {}
    def dfs(lst):
        if not lst:
            return True

        if lst[0] not in '()':
            return False
        if lst[0] == '(':
            return dfs(lst[1:])
        else:
            if len(lst) > 1:
                if lst[1] == ')':
                    return False
            return dfs(lst[2:])

    return 'Yes' if sum([len(lst) - len(lst.lstrip('(').rstrip(')')) - 2,
                                              len(lst) - len(lst.lstrip(')').rstrip('('))]) == 0 else 'No'


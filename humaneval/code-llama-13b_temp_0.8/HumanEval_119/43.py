
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
    # pass
    def is_match(a, b):
        if a == '(' and b == ')':
            return True
        return False

    def reverse(lst):
        res = ''
        for item in lst:
            if item == '(':
                res += ')'
            else:
                res += '('
        return res

    def is_good(lst):
        res = []
        for item in lst:
            if item == '(':
                res.append(item)
            else:
                if len(res) == 0:
                    return False
                if is_match(res.pop(), item):
                    continue
                else:
                    return False
        return len(res) == 0

    if len(lst) == 1:
        return 'Yes' if lst[0] == '()' else 'No'

    if len(lst) == 2:
        return 'Yes' if is_match(lst[0], lst[1]) else 'No'

    res = lst[0] + lst[1]
    if is_good(res):
        return 'Yes'
    else:
        res = reverse(lst[0]) + lst[1]
        if is_good(res):
            return 'Yes'
        else:
            return 'No'


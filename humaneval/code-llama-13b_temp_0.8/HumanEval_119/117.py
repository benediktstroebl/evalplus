
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
    def is_match(s1, s2):
        if s1 == '(' and s2 == ')' or s1 == ')' and s2 == ')':
            return True
        else:
            return False

    def is_good(s):
        if len(s) == 0:
            return True
        if s[0] == '(' and s[-1] == ')':
            return is_good(s[1:-1])
        else:
            return False

    if is_good(lst):
        return 'Yes'
    else:
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if is_match(lst[i], lst[j]):
                    s = lst[:i] + lst[i+1:j] + lst[j+1:]
                    if is_good(s):
                        return 'Yes'
        return 'No'


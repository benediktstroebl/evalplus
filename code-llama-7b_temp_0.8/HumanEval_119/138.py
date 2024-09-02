
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
    def is_balanced(lst):
        if not lst:
            return True

        result = []
        for x in lst:
            if x == '(':
                result.append(x)
            elif x == ')':
                if not result or result[-1] != '(':
                    return False
                result.pop()
        return len(result) == 0

    s1, s2 = lst
    if len(s1) == 0 and len(s2) == 0:
        return 'Yes'
    if len(s1) == 0:
        return 'Yes' if is_balanced(s2) else 'No'
    if len(s2) == 0:
        return 'Yes' if is_balanced(s1) else 'No'

    if len(s1) > len(s2):
        return match_parens([s2, s1])

    if is_balanced(s1 + s2):
        return 'Yes'

    if is_balanced(s1[:len(s1) // 2] + s2 + s1[len(s1) // 2:]):
        return 'Yes'

    if is_balanced(s2[:len(s2) // 2] + s1 + s2[len(s2) // 2:]):
        return 'Yes'

    return 'No'

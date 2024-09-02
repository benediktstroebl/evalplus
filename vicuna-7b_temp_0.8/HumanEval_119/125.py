
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
        return 'No'
    elif len(lst) == 1:
        return 'Yes'
    else:
        s1 = lst[0]
        s2 = lst[1]
        if s1 == '(' or s1 == ')':
            if s2 == '(' or s2 == ')':
                return 'Yes'
            else:
                for i in range(len(s1)):
                    if s1[i] == '(' and s2[i] == ')':
                        s1 = s1[:i] + s1[i+1:]
                        s2 = s2[:i] + s2[i+1:]
                        if match_parens([s1, s2]) == 'Yes':
                            return 'Yes'
                        else:
                            return 'No'
        return 'No'

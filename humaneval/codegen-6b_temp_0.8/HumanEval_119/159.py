
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
    str1, str2 = lst[0], lst[1]
    if len(str1) != len(str2):
        return "No"
    dict = [0 for i in xrange(len(str1))]
    for i in xrange(len(str1)):
        if str1[i] == ')':
            if  dict[i] == 0:
                return "No"
            while dict[i] != 0:
                if str1[i] != '(':
                    return "No"
                dict[i] -= 1
                i -= 1
        else:
            dict[i] += 1
    if sum(dict) != 0:
        return "No"
    return "Yes"


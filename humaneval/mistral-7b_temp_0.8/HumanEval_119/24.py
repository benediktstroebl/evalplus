
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
    s1, s2 = lst
    lst1 = list(s1)
    lst2 = list(s2)
    if len(lst1) > len(lst2):
        a, b = lst1, lst2
    else:
        a, b = lst2, lst1
    for i in range(len(a)):
        if a[i] == '(':
            for j in range(len(b)):
                if b[j] == ')':
                    a.pop(i)
                    b.pop(j)
                    break
    if a == '':
        return 'Yes'
    else:
        return 'No'



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
    lst2 = lst[:]
    lst2.reverse()
    if len(lst) != len(lst2):
        return 'No'
    d = {')': '(',
         '(': ')'}

    def check(lst1, lst2):
        if not lst1:
            return True
        if not lst2:
            return False
        lst1 = lst1[:]
        lst2 = lst2[:]
        for i in range(len(lst1)):
            if lst1[i] == d[lst2[i]]:
                lst1[i] = '#'
                lst2[i] = '#'
                if check(lst1, lst2):
                    return True
        return False
    if check(lst, lst2):
        return 'Yes'
    else:
        return 'No'

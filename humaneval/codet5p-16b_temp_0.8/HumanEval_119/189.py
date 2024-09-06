
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

    assert lst, 'Given list is empty!'
    assert all(i in ['(', ')'] for i in lst), 'Given list is not balanced!'
    lst1 = lst[0]
    lst2 = lst[1]
    out = []
    return_list = []
    out.append(lst1)
    out.append(lst2)
    return_list.append(out)
    out = []
    while True:
        if len(lst1) == 0:
            out.append('Yes')
            return_list.append(out)
            return return_list
        else:
            out.append(lst1)
            lst1 = []
            for i in lst1:
                out.append(i)
                lst1.remove(i)
        out.append(lst2)
        lst2 = []
        for i in lst2:
            out.append(i)
            lst2.remove(i)
        lst2 = out[-1]
        out = out[

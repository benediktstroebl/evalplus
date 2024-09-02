
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

    for i in range(len(lst)):
        if lst[i][0] == ')' and lst[i][-1] == '(':
            lst[i] = lst[i][:-1]
        elif lst[i][0] == '(' and lst[i][-1] == ')':
            lst[i] = lst[i][1:]

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                if lst[i][-1] == '(' and lst[j][0] == ')':
                    lst[i] = lst[i][:-1]
                    lst[j] = lst[j][1:]
                    break
                else:
                    continue
    if ')' in lst:
        return "No"
    else:
        return "Yes"

    #for i in lst:
     #   print(i)
    #return lst

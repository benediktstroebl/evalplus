
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
    #first slice of the list
    a = lst[0]
    #second slice of the list
    b = lst[1]
    #if both slices are empty
    if a=='' and b=='':
        return 'Yes'
    #if a is empty
    if a=='':
        if b.count('(')!=b.count(')'):
            return 'No'
        else:
            return 'Yes'
    #if b is empty
    if b=='':
        if a.count('(')!=a.count(')'):
            return 'No'
        else:
            return 'Yes'
    #counts the number of open and close parentheses in each slice
    a_open = a.count('(')
    a_close = a.count(')')
    b_open = b.count('(')
    b_close = b.count(')')
    #if difference of open and close parentheses is equal to 0, slice is balanced
    if a_open-a_close==0 and b_open-b_close==0:
        return 'Yes'
    #if they are equal and the difference is non-zero
    elif a_open-a_close==b_open-b_close and a_open-a_close!=0:
        return 'Yes'
    #if the difference is zero, concatenate and check again
    elif a_open-a_close==b_open-b_close==0:
        #concatenate
        lst[0] = a+b
        #check if it's balanced
        return match_parens(lst)
    else:
        return 'No'

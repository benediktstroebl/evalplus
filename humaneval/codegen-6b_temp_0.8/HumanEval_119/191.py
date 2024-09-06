
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
    if lst[0][-1] == ')' or lst[1][0] == '(' or lst[0][-2] == ')' or lst[1][1] == '(':
        return 'No'
    
    stack_lst =  lst[0][1:-1]
    stack_lst.reverse()
    stack_lst.append(lst[1])
    if match_parens_rec_helper(stack_lst, 0, len(stack_lst) - 1) == True:
        return 'Yes'
    else:
        return 'No'
    
    
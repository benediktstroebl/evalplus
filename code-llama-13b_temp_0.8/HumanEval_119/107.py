
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

    # Your code here
    # stack = [lst[0]]
    # while stack:
    #     if lst[1]:
    #         if lst[1][0] == ')' and stack[-1] == '(':
    #             stack.pop()
    #         else:
    #             stack.append(lst[1][0])
    #         lst[1] = lst[1][1:]
    #     else:
    #         return 'No'
    # return 'Yes'
    lst1, lst2 = lst[0], lst[1]
    res = ''
    while lst1:
        if lst1[-1] == ')' and lst2[0] == '(':
            res += ')'
            lst1 = lst1[:-1]
            lst2 = lst2[1:]
        else:
            res += '('
            lst1 = lst1[:-1]
    while lst2:
        if lst2[-1] == ')' and res[-1] == '(':
            res = res[:-1]
            lst2 = lst2[:-1]
        else:
            res += ')'
            lst2 = lst2[:-1]
    return 'No' if res else 'Yes'



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
    # This function uses recursion to find a solution.
    # Each time a pair of '()' is found the function is called again to find
    # a solution. If a solution is found it is returned, otherwise it returns
    # False.
    # Base case is when there are no more '()' pairs.
    # When a solution is found, it is added to a list.
    # All solutions are compared to the list, and if one is found then all
    # solutions are returned.
    lst_lst = []
    lst_lst.append(lst)
    while True:
        for lst_item in lst_lst:
            if '()' in lst_item:
                lst_item.remove('()')
                lst_item.append('')
                lst_lst.append(lst_item[:])
            else:
                return 'Yes'
        lst_lst = []
    if lst_lst == []:
        return 'No'




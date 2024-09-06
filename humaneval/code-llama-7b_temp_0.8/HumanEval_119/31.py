
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

    open_par = '('
    close_par = ')'

    def par_check(string):
        par_list = [open_par, close_par]
        check_str = ''
        for i in string:
            check_str += i
        for i in check_str:
            if i not in par_list:
                return 'No'
        stack = []
        for i in check_str:
            if i == open_par:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return 'No'
                stack.pop()
        return 'Yes'
    if par_check(lst[0]) == 'No' or par_check(lst[1]) == 'No':
        return 'No'
    else:
        return 'Yes'

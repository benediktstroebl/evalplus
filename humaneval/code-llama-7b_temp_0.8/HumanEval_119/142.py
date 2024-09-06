
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
    def recursive_call(lst):
        for i in range(len(lst)):
            if lst[i] == ')':
                if i - 1 >= 0 and lst[i - 1] == '(':
                    return True
                elif i - 1 >= 0 and lst[i - 1] == ')':
                    lst.pop(i - 1)
                    return recursive_call(lst)
        return False
    return 'Yes' if recursive_call(lst) else 'No'



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

    def paren_check(lst):
        paren_dict = {')': '(', '(': ')', '[': ']', ']': '['}
        open_parens = ['(', '[', '{']
        stack = []
        for elem in lst:
            if elem in open_parens:
                stack.append(elem)
            else:
                if stack == []:
                    return False
                if paren_dict[elem] != stack[-1]:
                    return False
                else:
                    stack.pop(-1)
        return True

    if len(lst) == 1:
        return 'Yes'
    if len(lst) == 2:
        return 'Yes' if paren_check(lst) else 'No'
    else:
        lst1 = lst[0:2]
        lst2 = lst[2:]
        if lst1 == [')', ')']:
            return 'No'
        if paren_check(lst1):
            lst1_result = 'Yes'
        else:
            lst1_result = 'No'
        if paren_check(lst2):
            lst2_result = 'Yes'
        else:
            lst2_result = 'No'
        if lst1_result == 'Yes' and lst2_result == 'Yes':
            return 'Yes'
        if lst1_result == 'Yes' and lst2_result == 'No':
            return 'Yes'
        if lst1_result == 'No' and lst2_result == 'Yes':
            return 'Yes'
        if lst1_result == 'No' and lst2_result == 'No':
            return 'No'



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

    
    def balance(s):
        stack = []
        for i in s:
            if i == ')':
                stack.append(')')
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False

    lst_of_strings = []
    for i in lst:
        lst_of_strings.append(list(i))

    lst_of_strings_1 = []
    for i in lst_of_strings:
        lst_of_strings_1.append(''.join(i))

    final = []
    for i in lst_of_strings_1:
        if balance(i) == True:
            final.append(i)

    if len(final) == 0:
        return 'No'
    else:
        return 'Yes'


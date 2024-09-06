
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
    if not any(lst):
        return 'No'

    # if there is only one element, it is guaranteed to be balanced and can be concatenated with the empty string
    if len(lst) == 1:
        return 'Yes'

    # if there are two elements, check if the first and second element can be concatenated in some order to form a good string
    if len(lst) == 2:
        first, second = lst
        if first == '(' and second == ')':
            return 'Yes'
        elif first == ')':
            return 'Yes'
        else:
            return 'No'

    # in case of more than two elements, we can check all possible combinations of the elements to check if any combination forms a good string
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            string = ''.join(lst[i*2:(i+1)*2])
            if string == '':
                # if the concatenation forms an empty string, the resulting string is not balanced and returns 'No'
                return 'No'
            elif string == '(' or string == ')':
                # if either of the elements is an open or close parenthesis, the resulting string is not balanced and returns 'No'
                return 'No'
            else:
                if match_parens(lst[:i] + [string, lst[i+1:]] + lst[i+2:]) == 'Yes':
                    return 'Yes'
    return 'No'
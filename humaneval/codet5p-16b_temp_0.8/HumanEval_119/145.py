
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

    if len(lst)!= 2:
        return "Invalid input"
    
    left, right = lst

    if right[0]!= left[-1]:
        return "No"

    left_count = right_count = 0

    for paren in left:
        if paren == '(':
            left_count += 1
        elif paren == ')':
            if left_count == 0:
                return "No"
            left_count -= 1
    
    for paren in right:
        if paren == '(':
            right_count += 1
        elif paren == ')':
            if right_count == 0:
                return "No"
            right_count -= 1
    
    if left_count!= 0 or right_count!= 0:
        return "No"
    return "Yes"
    


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
    # your code here

    # check that the string is balanced, for each open parenthesis,
    # there is a close parenthesis, same amount
    # if not balanced, return 'No'
    # for each '(', check if there is a matching ')'
    # if there is no matching ')', return 'No'
    # if there are more ')' than '(', return 'No'
    # if we find a match, pop the matching ')' and move to next character
    # if there are no more characters to match, return 'Yes'

    # stack
    # pop characters from lst, add to stack
    # check if the next char is a match
    # if it is, pop the matching paren
    # if we run out of characters before stack is empty, return 'No'
    # if stack is empty before we run out of chars, return 'Yes'
    # if we find a char that doesn't match, return 'No'

    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst
    # for each character in lst

    # connect each character with its matching character
    # check if the list is balanced

    # step through the list
    # step through the list

    # check if there are matching parentheses
    # for each '(', find if there is a matching ')'

    # if we find a matching ')'
    # if we run out of characters
    # if we find a character that doesn't match

    # add open paren to a list
    # check if the next char is a close paren
    # if it is, pop the matching paren
    # if we run out of characters before stack is empty, return 'No'
    # if stack is empty before we run out of chars, return 'Yes'
    # if we find a char that doesn'

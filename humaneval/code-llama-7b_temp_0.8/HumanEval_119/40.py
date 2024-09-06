
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
    # find match for opening paren
    # find match for closing paren
    # if no match, return False
    # if no closing paren, add it to start of string
    # if no opening paren, add it to end of string
    # check if remaining parens in string are balanced
    # if not, return False
    # return True

    string_one = lst[0]
    string_two = lst[1]
    string_one_reversed = string_one[::-1]
    string_two_reversed = string_two[::-1]
    print(string_one_reversed)
    print(string_two_reversed)
    balanced_string_one = balance(string_one_reversed)
    balanced_string_two = balance(string_two_reversed)
    print(balanced_string_one)
    print(balanced_string_two)


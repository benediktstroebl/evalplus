
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

    # Create a function that returns a list with all the opening and closing
    # parentheses in the string.
    def count_parens(string):
        opening_parens = []
        closing_parens = []
        for character in string:
            if character == '(':
                opening_parens.append(character)
            else:
                closing_parens.append(character)
        return opening_parens, closing_parens

    # Check if there are an even number of parentheses in the string.
    if len(lst[0]) % 2 != 0:
        return 'No'

    # Check if the opening parentheses match up with the closing parentheses.
    for index, opening_parenthesis in enumerate(lst[0]):
        if opening_parenthesis == '(':
            if index + 1 >= len(lst[0]):
                return 'No'
            else:
                if lst[0][index + 1] != ')':
                    return 'No'
        if opening_parenthesis == ')

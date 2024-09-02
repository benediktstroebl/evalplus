
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

    # What is the expected output?
    # An example is not always a good thing to show.
    # For this question, you should show your expectation and why it should be so.
    # in this case, I think that a good string has an equal amount of open
    # and close parentheses.
    # I will consider a string to be good if it has an equal amount of open and close parentheses.
    # If we add an '(' and an ')', then the total number of open parentheses will
    # be one more than the number of close parentheses, and the string will be good.
    # If we add a ')' and a '(', then the total number of open parentheses will
    # be one less than the number of close parentheses, and the string will be good.
    # If we add a '(', and we do not add a corresponding ')', then the string will
    # be bad.
    # If we add a ')', and we do not add a corresponding '(', then the string will
    # be bad.
    # If we do not add anything, then we get an equal amount of open and close parentheses,
    # and we are already in a good state.

    # Brute Force
    # Check all possible string by using all the characters in the list.
    # Time Complexity: O(2^(n*m))

    # return 'Yes' if we found a good string.
    # return 'No' if we did not find a good string.
    # n = len(lst)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         result = lst[i] + lst[j]
    #         if result.count('(') == result.count(')'):
    #             return 'Yes'
    # return 'No'

    # Faster Way
    # Keep track of the number of open parentheses.
    # If the total number of open parentheses is odd, then the string is bad.
    # Otherwise, if we add an open parenthesis, then the total number of open
    # parentheses will be one more than the number of close parentheses, and the
    # string will be good.
    # If we add a close parenthesis, then the total

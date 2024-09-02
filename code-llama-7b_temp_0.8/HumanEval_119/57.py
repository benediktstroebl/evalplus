
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
    # Open: '(',  Close: ')'
    open, close = '(', ')'
    # Extract the strings from the list
    first, second = lst
    # The strings are not long enough, they are not good
    if len(first) < len(second):
        return 'No'

    # Initialize the counters for '(' and ')'
    first_count, second_count = 0, 0
    # Initialize a boolean flag, telling if the strings are good
    flag = True

    # Loop over the first string
    for i in range(len(first)):
        # Increment the counter for '('
        if first[i] == open:
            first_count += 1
        # Increment the counter for ')'
        elif first[i] == close:
            # If there are more close brackets than open, they are not good
            if first_count < 1:
                flag = False
                break
            # Decrement the counter for '('
            first_count -= 1

    # If the first string is not good, return No
    if not flag:
        return 'No'

    # The counters are the same at the beginning, the strings are good
    if first_count == second_count:
        return 'Yes'

    # The first string is good and the counters are not the same,
    # so the second string is not good
    flag = False
    # Loop over the second string
    for i in range(len(second)):
        # Increment the counter for '('
        if second[i] == open:
            second_count += 1
        # Increment the counter for ')'
        elif second[i] == close:
            # If there are more close brackets than open, they are not good
            if second_count < 1:
                flag = False
                break
            # Decrement the counter for '('
            second_count -= 1

    # If the second string is not good, return No
    if not flag:
        return 'No'

    # If we reach this point, the strings are good
    return 'Yes'


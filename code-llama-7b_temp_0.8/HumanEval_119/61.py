
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
    # first, we check the length of the input
    # input is a list of two strings
    # now we check if the lengths of the strings are the same.
    # if so, we return "no".  If not, we continue.
    if len(lst) != 2:
        return "No"
    elif len(lst[0]) != len(lst[1]):
        return "No"
    else:
        # now we are going to create a variable that will hold the
        # count of open parentheses in the string
        open_par = 0
        # now we iterate through the two strings
        for i in lst:
            # for the string, we create a variable to keep track of
            # the count of open parentheses
            par = 0
            # now we iterate through the string
            for j in i:
                # if the character is an open paren, we add one to our
                # count of open parens
                if j == '(':
                    par += 1
                # if the character is a close paren, we subtract one
                # from our count of open parens
                elif j == ')':
                    par -= 1
                # if the character is anything else, we add zero to our
                # count of open parens, which does nothing
                else:
                    par += 0
            # now we check if the count of open parens is zero or not
            if par != 0:
                return "No"
        return "Yes"

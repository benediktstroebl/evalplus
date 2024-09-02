
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
    ourstack = []
    theirstack = []

    for x in lst:
            #print('ourstack', ourstack)
            #print('theirstack', theirstack)

            #push all open parentheses to ourstack
            if x[0] == '(':
                    ourstack.append(x)
            #if we have a closing parenthesis and we are looking at a closing parenthesis
            #then we will see if our stack is the same as the closing parenthesis's stack
            elif x[len(x)-1] == ')' and len(ourstack) > 0:
                    if ourstack == theirstack:
                            return 'Yes'
                    #if we do not have the matching parenthesis, then we return 'No'
                    else:
                            return 'No'
            #if we have a closing parenthesis, and we do not have an open parenthesis
            #then we will see if our stack is the same as their stack
            elif x[len(x)-1] == ')' and len(ourstack) == 0:
                    return 'No'
            #pop a char off theirstack, and put it on ourstack
            else:
                    theirstack.append(x)
    #once we finish the loop, we will see if ourstack is the same as theirstack
    if ourstack == theirstack:
        return 'Yes'
    else:
        return 'No'

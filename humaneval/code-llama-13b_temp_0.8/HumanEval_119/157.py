
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
    # solve
    # return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
    # must be careful to only pop when we know we will have a closing
    # parentheses
    
    def helper(lst1, lst2):
        # lst1 is the list of open parantheses
        # lst2 is the list of close parantheses
        # recursively checks if we can make a good string
        if not lst1 or not lst2:
            # if either list is empty, return no
            return 'No'
        if lst1[-1] == lst2[-1]:
            # if the last two elements are equal,
            # remove the last elements of both and recurse
            lst1.pop()
            lst2.pop()
            return helper(lst1, lst2)
        else:
            # if the last two elements are not equal
            # pop the first element from lst1, append to lst2, and recurse
            lst1.pop()
            lst2.append(lst1[-1])
            return helper(lst1, lst2)
    
    # if we can make a good string, return yes, otherwise return no
    return helper(lst[::2], lst[1::2]) if lst[0] == '(' else helper(lst[1::2], lst[::2])

    
    

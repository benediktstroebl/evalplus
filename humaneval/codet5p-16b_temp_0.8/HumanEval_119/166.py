
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

    
    def count(lst):
        '''
        Count the number of open and close parentheses in a given list.

        Examples:
        >>> count([])
        0
        >>> count(['(', ')'])
        1
        >>> count(['(', '(', ')', ')'])
        3
        '''
        
        count = 0
        for e in lst:
            if e == '(':
                count += 1
            elif e == ')':
                count -= 1
        return count

    def match(lst):
        '''
        Match the open parentheses '(' and close parentheses ')' in a list.

        Examples:
        >>> match([')', ')'])
        'No'
        >>> match(['(', ')'])
        'Yes'
        >>> match(['(', '(', ')', ')'])
        'Yes'
        >>> match(['(', '(', ')', ')', ')'])
        'No'
        '''
        
        count = count(lst)
        if count > 0:
            


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

    def is_balanced(str):
        #track open parentheses
        open_count = 0
        for ch in str:
            #increment open count if open parenthesis
            if ch == '(':
                open_count += 1
            else:
                #decrement open count if close parenthesis
                open_count -= 1
        return open_count == 0

    def is_concat(str1, str2):
        #check if concatenating str1 and str2 will give us a balanced string
        str3 = str1+str2
        #if concatenating str1 and str2 will give us a balanced string,
        #then we can concatenate them and get a balanced string
        if is_balanced(str3):
            return 'Yes'
        else:
            return 'No'
    return is_concat(lst[0], lst[1])

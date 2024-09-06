
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

    # Check that a string is good
    def good(str):
        return str.count('(') == str.count(')')

    # Merge two strings
    def merge(str1, str2):
        return str1 + str2

    # Concat the strings in each list
    def concat(lst):
        return [merge(lst[0], lst[1]), merge(lst[1], lst[0])]

    # Apply merge until no changes
    def reduce(lst):
        changes = True
        while changes:
            changes = False
            new_lst = []
            for item in lst:
                if len(item) == 1:
                    new_lst.append(item)
                else:
                    new_lst += concat(item)
                    changes = True
            lst = new_lst
        return lst

    # Main function
    lst = reduce(lst)
    for item in lst:
        if not good(item):
            return 'No'
    return 'Yes'

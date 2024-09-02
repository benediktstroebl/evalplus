
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
    # This method works by building a list of nested 'stacks'. Each stack
    # contains a list of open parentheses with the same number of elements as
    # the number of close parentheses (must be the same number because these
    # are the only characters we have to work with). As each open parenthesis
    # is added to a stack, the number of open parentheses is decremented;
    # when a close parenthesis is added, the number of close parentheses is
    # decremented. The number of open parentheses must be 0 at the end of the
    # string in order for it to be good; the number of close parentheses must
    # be 0 at the end of the string in order for the number of open
    # parentheses to remain 0.
    # This method assumes that the number of parentheses will be the same for
    # both strings (if they aren't, the strings can't be appended to make a
    # good string)
    stacks = [[] for _ in lst]
    open_parens = []
    for idx, string in enumerate(lst):
        for char in string:
            if char == '(':
                open_parens.append(char)
                stacks[idx].append(open_parens.pop())
            elif char == ')':
                if stacks[idx]:
                    stacks[idx].pop()
                elif open_parens:
                    open_parens.pop()
                else:
                    return 'No'
    if sum(len(stack) for stack in stacks) == 0 and all(not stack for stack in stacks):
        return 'Yes'
    else:
        return 'No'

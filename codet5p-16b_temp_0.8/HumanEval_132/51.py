
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''

    brackets = []
    
    for bracket in string:
        if bracket == '[' or bracket == ']':
            brackets.append(bracket)

    nested = False

    if len(brackets) <= 2:
        return False

    for index, bracket in enumerate(brackets):
        if bracket == ']' and nested == False:
            nested = True
        elif bracket == '[' and nested == True:
            return True
        else:
            nested = False

    return False


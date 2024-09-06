
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

    bracket = []
    for i in string:
        if i == '[':
            bracket.append('[')
        elif i == ']':
            if len(bracket) == 0:
                return False
            elif bracket[-1] == '[':
                bracket.pop()
    if len(bracket) == 0:
        return True
    else:
        return False


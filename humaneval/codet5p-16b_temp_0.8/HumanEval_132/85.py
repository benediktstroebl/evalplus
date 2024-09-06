
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

    bracket = ''
    for s in string:
        if s == '[':
            bracket += s
        elif s == ']':
            bracket += s
            if not bracket:
                return False
            elif bracket[-2] == '[':
                return True
            else:
                bracket = bracket[:-1]
    return False


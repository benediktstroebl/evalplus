
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
    if len(string) < 2:
        return False

    openers = 0
    closers = 0

    for bracket in string:
        if bracket == '{':
            openers += 1
        elif bracket == '}':
            if openers > 0:
                openers -= 1
            else:
                return False
        elif bracket == '[':
            closers += 1
        elif bracket == ']':
            if closers > 0:
                closers -= 1
            else:
                return False

    return openers == 0 and closers == 0

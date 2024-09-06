
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
    def is_nested_inner(string, i=0, opened=0, closed=0):
        if i >= len(string):
            return False
        if string[i] == '[':
            opened += 1
        elif string[i] == ']':
            closed += 1
        if opened - closed < 0:
            return False
        return is_nested_inner(string, i + 1, opened, closed)
    return is_nested_inner(string)


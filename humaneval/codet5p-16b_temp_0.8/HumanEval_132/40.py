
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

    def is_nested_helper(i):
        open = 0
        closed = 0
        for j in range(i, len(string)):
            if string[j] == '[':
                open += 1
            elif string[j] == ']':
                closed += 1
            if closed > open:
                return False
            elif closed == open:
                return is_nested_helper(j + 1)
        return True

    return is_nested_helper(0)
    
    

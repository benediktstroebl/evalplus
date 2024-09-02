
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

    bracket_stack = []

    for bracket in string:
        if bracket == '[':
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) == 0:
                return False
            else:
                bracket_stack.pop()
        
    if len(bracket_stack) == 0:
        return True
    else:
        return False


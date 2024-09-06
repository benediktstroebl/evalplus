
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
    is_nested = False

    for bracket in string:
        if bracket == '[':
            brackets.append(bracket)
        elif bracket == ']' and len(brackets) > 0:
            brackets.pop()
            is_nested = True
        else:
            return False

    return not bool(brackets) and is_nested
    

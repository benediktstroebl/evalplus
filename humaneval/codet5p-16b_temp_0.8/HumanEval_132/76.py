
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

    if string[0] == '[':
        return is_nested(string[1:])
    elif string[0] == ']':
        return False
    else:
        open = 0
        for i, char in enumerate(string[1:]):
            if char == '[' and open == 0:
                return is_nested(string[i+2:])
            elif char == ']' and open == 0:
                return False
            elif char == ']' and open == 1:
                open -= 1
            elif char == '[' and open == 1:
                open += 1
    return False




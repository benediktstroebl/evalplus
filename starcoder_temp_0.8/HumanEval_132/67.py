
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

    # # MUCH SIMPLER SOLUTION
    # if (
    #     not string
    #     or string == '[]'
    #     or string == '[[]'
    #     or string == '[][]'
    # ):
    #     return False
    # if string[0] == ']':
    #     return True
    # elif string[0] == '[':
    #     for i in range(1, len(string)):
    #         if string[i] == ']':
    #             return True
    #         elif string[i] == '[':
    #             return is_nested(string[i:])
    # return False

    if not string:
        return False
    elif len(string) == 1:
        if string == ']':
            return False
        elif string == '[':
            return True
    elif string[0] == ']':
        return False
    elif string[0] == '[':
        for i in range(1, len(string)):
            if string[i] == ']':
                return False
            elif string[i] == '[':
                return is_nested(string[i:])
    return False

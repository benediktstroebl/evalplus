
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

    def is_bracket(string):
        if string == '':
            return False
        else:
            if string[0] == '[':
                return is_bracket(string[1:])
            else:
                return False

    def is_nested_bracket(string):
        if string == '':
            return False
        elif string[0] == '[':
            return is_nested_bracket(string[1:])
        else:
            return is_bracket(string)

    return is_nested_bracket(string)


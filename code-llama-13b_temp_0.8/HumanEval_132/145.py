
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
    def check(string):
        if string == '':
            return False
        if string[0] != '[' and string[-1] != ']':
            return False
        if len(string) == 2:
            return True
        substrings = string[1:-1].split(']')
        for str in substrings:
            if len(str) == 0:
                return False
            if str[0] == '[' and len(str) != 1:
                if not check(str[1:]):
                    return False
            elif str[-1] == '[' and len(str) != 1:
                if not check(str[:-1]):
                    return False
            else:
                return False
        return True
    return check(string)




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
    if len(string) == 2:
        return string == '[]'
    if string[0] != '[' or string[-1] != ']':
        return False
    else:
        i = 1
        count = 0
        while i < len(string)-1:
            if string[i] == '[':
                count += 1
            elif string[i] == ']':
                count -= 1
                if count < 0:
                    return False
            i += 1
    return count == 0


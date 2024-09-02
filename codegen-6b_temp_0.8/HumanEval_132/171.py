
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
    length = len(string)
    index = 0
    while index != length:
        if string[index] == '[':
            if index + 1 < length and string[index + 1] == '[':
                index += 2
                continue
            else:
                return False
        if string[index] == ']':
            if index + 1 < length and string[index + 1] == ']':
                index += 2
                continue
            else:
                return False

        index += 1
    return True


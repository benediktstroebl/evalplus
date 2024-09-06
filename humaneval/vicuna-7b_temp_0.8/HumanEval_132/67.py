
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
    current_size = 0
    nested = False
    for i in range(len(string)):
        if string[i:i+2] == '[]':
            if nested is True:
                nested = False
            else:
                current_size += 1
                nested = True
        elif string[i:i+2] == ']':
            if nested is True:
                nested = False
                current_size -= 1
            else:
                current_size += 1
        elif string[i:i+2] == '[':
            nested = True
        else:
            raise ValueError('Invalid input')
    return nested or current_size >= 2
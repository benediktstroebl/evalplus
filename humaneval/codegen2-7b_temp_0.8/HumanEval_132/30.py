
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
    is_nested = True
    array = string.split('][')
    for i in range(len(array)):
        if (len(array[i]) == 0):
            is_nested = False
            break
        elif (array[i][0] == '['):
            if (is_nested == False):
                break
            else:
                is_nested = is_nested and is_nested(array[i][1:])
    return is_n

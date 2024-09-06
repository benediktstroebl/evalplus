
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
    brackets = {}
    for i in range(len(string)):
        if string[i] == '[':
            brackets['left'] = i
        else:
            brackets['right'] = i
            if (brackets['left'] - brackets['right']) % 2 == 0 and brackets['left'] - brackets['right'] >= 2:
                return True

    return False


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
        if string[0] == '[' and string[1] == ']':
            return False
    start = False
    count = 0
    for i in string:
        if i == '[':
            if count == 0:
                start = True
            count += 1
        elif i == ']':
            if count == 0:
                return False
            count -= 1
            if count == 0 and start:
                return True
    return False



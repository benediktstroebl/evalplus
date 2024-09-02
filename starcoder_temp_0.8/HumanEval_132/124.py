
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
    s = []
    for i in range(len(string)):
        if string[i] == '[':
            s.append(string[i])
        elif string[i] == ']':
            if len(s) == 0:
                return False
            else:
                s.pop(-1)
    return len(s) == 0


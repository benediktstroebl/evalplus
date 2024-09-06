
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
    string = string.replace('[','')
    string = string.replace(']','')
    left = 0
    right = 0
    for i in range(0, len(string)):
        if string[i] == '(':
            left += 1
        elif string[i] == ')':
            right += 1
            if left == right:
                return True
            elif left > right:
                return False
    if left == right:
        return True
    return False












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
    if string[0] == '[':
        left = string[1:].index(']') + 2
    else:
        left = string.index('[') + 1

    if string[left:len(string) - 1] == string[left:len(string) - 1][::-1]:
        return True
    else:
        return False


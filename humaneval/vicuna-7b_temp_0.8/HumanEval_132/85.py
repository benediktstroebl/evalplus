
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
    nested = 0
    for i in range(len(string)):
        if string[i] == '[' and nested % 2 == 0:
            nested += 1
        elif string[i] == ']' and nested % 2 == 1:
            nested -= 1
        elif nested % 2 != 0:
            return True
    return False


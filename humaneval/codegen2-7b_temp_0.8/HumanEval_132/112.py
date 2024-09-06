
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
    array = []
    for i in range(len(string)):
        if string[i] == '[':
            if len(array) > 0 and array[-1] == ']':
                array.pop()
            else:
                array.append(string[i])
        if string[i] == ']':
            if len(array) > 0 and array[-1] == '[':
                array.pop()
            else:
                array.append(string[i])
    return len(array) > 0


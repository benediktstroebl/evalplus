
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
    string = string.replace(' ', '')
    if string == '':
        return False

    opening = []
    closing = []
    for i in string:
        if i == '[':
            opening.append(i)
        elif i == ']':
            closing.append(i)

    for i in opening:
        if i not in closing:
            return False
    return True

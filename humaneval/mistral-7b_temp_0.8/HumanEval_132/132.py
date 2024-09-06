
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
    list = []
    for i in string:
        list.append(i)
    if len(list) > 1:
        if list[0] == list[-1]:
            return False
        elif list[0] == '[' and list[-1] == ']':
            return True
        else:
            return False
    else:
        return False

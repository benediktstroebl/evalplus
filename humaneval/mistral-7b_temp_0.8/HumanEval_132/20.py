
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
    length = len(string)
    i = 0
    brackets_list = []
    brackets_list.append(string[i])
    while i < length:
        if string[i] == '[':
            brackets_list.append(string[i])
        if string[i] == ']':
            if string[i] == brackets_list[-1]:
                brackets_list.pop()
                i += 1
            else:
                return False
        else:
            return False
        i += 1
    return brackets_list

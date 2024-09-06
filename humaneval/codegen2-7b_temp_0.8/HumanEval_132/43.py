
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
    list_ = []
    for i in range(len(string)):
        if string[i] == '[' or string[i] == '{' or string[i] == '(':
            list_.append(string[i])
        if string[i] == ']' or string[i] == '}' or string[i] == ')':
            if list_[-1] == '[' or list_[-1] == '{' or list_[-1] == '(':
                list_.pop()
            else:
                return False
    return True

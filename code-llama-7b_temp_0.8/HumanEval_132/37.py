
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
    if len(string) < 4: return False
    open_flag, close_flag = False, False
    for i in range(len(string)):
        if string[i] == '[':
            if open_flag == False: open_flag = True
            else: open_flag = False
            if close_flag == True: return True
        if string[i] == ']':
            if close_flag == False: close_flag = True
            else: close_flag = False
            if open_flag == True: return True
    return False

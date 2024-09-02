
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
    # init
    #bracket_l = '[['
    #bracket_r = ']]'
    open_cnt = 0
    for elm in string:
        if elm == '[':
            open_cnt += 1
        if elm == ']':
            open_cnt -= 1
        if open_cnt < 0:
            return True
    return False



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
    s_list = list(string)
    n = len(s_list)
    count_open = 0
    count_closed = 0
    for x in range(n):
        if s_list[x] == '[':
            count_open += 1
        else:
            count_closed += 1
        if count_closed > count_open:
            return False
    return True
    

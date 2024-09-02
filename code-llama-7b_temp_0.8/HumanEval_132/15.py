
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
    #count = 0
    #for i in string:
    #    if i == '[':
    #        count += 1
    #    elif i == ']':
    #        count -= 1
    #    if count < 0:
    #        return True
    #return False
    
    # nested = False
    # for i in range(len(string)):
    #     if string[i] == '[':
    #         if not nested:
    #             nested = True
    #     elif string[i] == ']':
    #         nested = False
    #     if nested and (i == len(string) - 1):
    #         return True
    # return False
    
    open_cnt = 0
    for i in string:
        if i == '[':
            open_cnt += 1
        elif i == ']':
            open_cnt -= 1
        if open_cnt < 0:
            return True
    return False

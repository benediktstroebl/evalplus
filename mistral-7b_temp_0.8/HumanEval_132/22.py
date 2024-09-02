
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
    # if len(string)==0:
    #     return False
    # else:
    #     if string[0]=='[' and string[-1]==']':
    #         return True
    #     else:
    #         return False
    # for i in range(len(string)):
    #     if string[i]=='[' and string[-1]==']':
    #         return True
    #     else:
    #         return False
    # return False

    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        else:
            count -= 1
    return count == 0

    return True if string.count('[') == string.count(']') else False

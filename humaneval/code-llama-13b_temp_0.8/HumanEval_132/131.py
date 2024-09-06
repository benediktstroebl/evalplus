
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
    # 1st solution
    check = []
    for i in string:
        if i == ']':
            if check.pop() == '[':
                continue
            return False
        check.append(i)
    return True

    # 2nd solution
    # stack = []
    # for i in string:
    #     if i == '[':
    #         stack.append(i)
    #         continue
    #     elif not stack:
    #         return False
    #     elif stack.pop() == '[':
    #         continue
    #     else:
    #         return False
    # return not stack

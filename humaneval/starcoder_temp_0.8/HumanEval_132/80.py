
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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # simple first solution, not good, O(n^2)

    # for i in range(len(string)-1):
    #     if string[i] == '[' and string[i+1] == ']':
    #         return True
    #     elif string[i] == ']':
    #         return False
    #     elif string[i] == '[' and string[i+1] == '[':
    #         for j in range(i+1, len(string)-1):
    #             if string[j] == '[' and string[j+1] == ']':
    #                 return True

    # return False

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # second solution, O(n)

    level = 0
    for i in range(len(string)):
        if string[i] == '[':
            level += 1
        if string[i] == ']':
            if level == 0:
                return False
            level -= 1
    return level == 0

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

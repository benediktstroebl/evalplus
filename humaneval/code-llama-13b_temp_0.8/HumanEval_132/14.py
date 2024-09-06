
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
    # if len(string)%2 != 0:
    #     return False
    # if len(string) <= 1:
    #     return False
    # else:
    #     if string[0] == '[':
    #         if string[-1] == ']':
    #             # print('a')
    #             for index, c in enumerate(string[1:-1]):
    #                 # print(index)
    #                 if c == ']':
    #                     # print(string[index-1], c)
    #                     if string[index-1] == '[':
    #                         # print('b')
    #                         return True
    #                     else:
    #                         # print('c')
    #                         return False
    #             return False
    #         else:
    #             return False
    #     else:
    #         return False
    # return False
    stack = []
    for c in string:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

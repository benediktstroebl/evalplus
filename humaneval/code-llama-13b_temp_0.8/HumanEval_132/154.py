
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
    # list = []
    # if len(string) % 2 == 0:
    #     for i in string:
    #         if i == '[':
    #             list.append(i)
    #         elif i == ']':
    #             if len(list) == 0:
    #                 return False
    #             else:
    #                 list.pop()
    #     return len(list) == 0
    # else:
    #     return False
    return string.count(']') > string.count('[')


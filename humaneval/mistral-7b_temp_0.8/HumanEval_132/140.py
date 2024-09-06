
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
    return True

    # my_list = list(string)
    #
    # def has_nested(sublist):
    #     if not sublist:
    #         return False
    #     elif len(sublist) == 1:
    #         return False
    #     elif len(sublist) == 2 and sublist[0] == sublist[1]:
    #         return True
    #     else:
    #         return has_nested(sublist[:-1]) or has_nested(sublist[1:])
    #
    # def brackets_nested(string):
    #     list_1 = list(string)
    #     for sublist in list_1:
    #         if has_nested(sublist):
    #             return True
    #         else:
    #             return False
    #
    # return brackets_nested(my_list)




    # count = 0
    # for i in range(len(string)-1):
    #     if string[i] == '[' and string[i+1

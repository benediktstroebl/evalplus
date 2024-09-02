
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
    ##  1st solution
    # i = 0
    # while i < len(string):
    #     # if string[i] == '[':
    #     #     check_if_nested = True
    #     #     counter = 0
    #     #     for el in string[i+1:]:
    #     #         if el == ']':
    #     #             counter += 1
    #     #         elif el == '[':
    #     #             if counter >= 1:
    #     #                 check_if_nested = False
    #     #             break
    #     #     if check_if_nested == True:
    #     #         return True
    #     # i += 1
    #     if ']' in string:
    #         check_if_nested = True
    #         counter = 0
    #         for el in string[string.index(']')+1:]:
    #             if el == ']':
    #                 counter += 1
    #             elif el == '[':
    #                 if counter >= 1:
    #                     check_if_nested = False
    #                 break
    #         if check_if_nested == True:
    #             return True
    
    ##  2nd solution
    # i = 0
    # while i < len(string):
    #     if string[i] == ']':
    #         check_if_nested = True
    #         counter = 0
    #         for el in string[i+1:]:
    #             if el == ']':
    #                 counter += 1
    #             elif el == '[':
    #                 if counter >= 1:
    #                     check_if_nested = False
    #                 break
    #         if check_if_nested == True:
    #             return True
    #     i += 1
    # return False

    ##  3rd solution
    i = 0
    while i < len(string):
        if string[i] == ']':
            check_if_nested = True
            counter = 0
            for el in string[

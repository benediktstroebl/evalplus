
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
    
    # if len(string) <= 1:
    #     return False
    # if len(string) %2 != 0:
    #     return False
    # check_bracket = []
    # for index,value in enumerate(string):
    #     if value=='[' or value==']':
    #         check_bracket.append(value)
    #     if len(check_bracket) %2 != 0:
    #         return False
    # if len(check_bracket) == 0:
    #     return True
    # return False
    # pass 

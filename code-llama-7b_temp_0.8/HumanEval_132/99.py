
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
    # My solution
    # ===========
    # if len(string) % 2 == 0:
    #     return False
    # count = 0
    # for i, s in enumerate(string):
    #     if s == '[':
    #         count += 1
    #     elif s == ']':
    #         count -= 1
    #     if count < 0:
    #         return True
    # return False
    
    # Other solutions
    # ===============
    # return True if len(string) % 2 == 1 and sum(s == '[' for s in string) > sum(s == ']' for s in string) else False
    
    # return len(string) % 2 == 1 and [string.index(s) for s in string if s == ']'].count(0) > [string.index(s) for s in string if s == '['].count(0)

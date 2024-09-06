
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
    
    if len(string)%2 != 0:
        return False
    check_for_opening = list(range(0,len(string),2))
    check_for_closing = list(range(1,len(string),2))
    nest = 0
    for i,pair in enumerate(zip(check_for_opening,check_for_closing)):
        if (pair[0]+1-nest) == pair[1]:
            nest = nest + 1
        else:
            return False
    return True

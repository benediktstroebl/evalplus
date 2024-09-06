
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
    def str_parse(string):
        if len(string) == 2:
            return 1
        elif string[0] != string[-1]:
            return 0
        else:
            return 1 + str_parse(string[1:-1])
    return 1 if str_parse(string) == 0 else 0
    
    

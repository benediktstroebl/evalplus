
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
    def check(string, count, brackets_list):
        if len(string) == 0:
            return count == 0
        elif string[0] == '[':
            return check(string[1:], count+1, brackets_list + [string[0]])
        elif string[0] == ']':
            if brackets_list[-1] == '[':
                return check(string[1:], count-1, brackets_list[:-1])
            else:
                return check(string[1:], count, brackets_list + [string[0]])
    return check(string, 0, [])
    

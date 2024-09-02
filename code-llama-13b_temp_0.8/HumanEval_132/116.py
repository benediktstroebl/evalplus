
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
    if '[' not in string or ']' not in string:
        return False
    else:
        open_count = 0
        for x in string:
            if x == '[':
                open_count += 1
            elif x == ']':
                if open_count == 0:
                    return False
                else:
                    open_count -= 1
        if open_count == 0:
            return True
        else:
            return False



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

    
    def is_square(s):
        return all(c in '[]' for c in s)
    
    def is_nested_recurse(string):
        if string == '':
            return True
        if string[0] in '[]':
            if is_square(string):
                return False
            else:
                return is_nested_recurse(string[1:])
        else:
            return is_nested_recurse(string[1:])
    
    return is_nested_recurse(string)


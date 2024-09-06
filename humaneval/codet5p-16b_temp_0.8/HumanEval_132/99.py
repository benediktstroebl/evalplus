
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

    
    def validate_brackets(bracket):
        open = 0
        close = 0
        for i in bracket:
            if i == '[':
                open += 1
            elif i == ']':
                close += 1
            if close > open:
                return False
        return True
    
    return validate_brackets(string)

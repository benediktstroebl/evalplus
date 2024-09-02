
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
    print('\n')
    print('string:', string)
    
    def match(open, close):
        print('\n')
        print('open:', open)
        print('close:', close)
        if open > close:
            return False
        if open == close:
            return True
        else:
            return match(open + 1, close - 1)
    
    if len(string) % 2 == 1:
        return False
    else:
        return match(0, len(string))


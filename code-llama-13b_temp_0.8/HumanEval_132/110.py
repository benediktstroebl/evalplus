
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
    def scan(string, opened, closed):
        # print(string, opened, closed)
        if not string:
            return closed >= 0
        if string[0] == '[':
            return scan(string[1:], opened + 1, closed)
        else:
            if opened == 0:
                return False
            return scan(string[1:], opened - 1, closed + 1)
    
    return scan(string, 0, 0)



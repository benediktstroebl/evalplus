
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

    if len(string) < 2:
        return False
    
    while string:
        opened = 0
        for i in range(len(string)):
            if string[i] == '[':
                opened += 1
            else:
                opened -= 1
            
            if opened == 0:
                if i == len(string) - 1:
                    return True
                string = string[i + 1:]
                break
            
    return False
            

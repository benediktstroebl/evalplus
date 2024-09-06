
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

    brackets = []
    for i in range(len(string)):
        if string[i] == '[' or string[i] == ']':
            brackets.append(string[i])
    
    if not len(brackets) % 2:
        if is_nested(string[1:-1]):
            return True
        else:
            return False
    else:
        return False
    


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
    string = list(string)
    nesting = 0
    for i in range(len(string)):
        if string[i] == '[':
            nesting += 1
        elif string[i] == ']':
            nesting -= 1
            if nesting < 0:
                nesting = 0
        elif string[i] == '[' and nesting > 0:
            nesting += 1
    return nesting > 0
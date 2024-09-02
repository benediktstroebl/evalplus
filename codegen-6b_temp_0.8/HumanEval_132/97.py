
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
    if len(string) == 0:
        return True
    if len(string) == 1:
        return False
    def bracket_find(string, pos):
        if pos == -1:
            return False
        if string[pos] == '[':
            return True
        return bracket_find(string, pos+1)
    result = bracket_find(string, 0)
    for i in range(pos+1, len(string)):
        if bracket_find(string, i) == False:
            return True
    return False
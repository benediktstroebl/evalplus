
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
    s = [char for char in string]
    count = 0
    for i, char in enumerate(s):
        if char == '[':
            count += 1
            if count == 2:
                return True
        elif char == ']':
            count -= 1
            if count == 1:
                return True
    if count > 0:
        return False

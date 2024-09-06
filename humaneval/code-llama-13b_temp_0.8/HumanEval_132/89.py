
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
    # Write your code here
    if string == '[]':
        return False
    
    open_count = 0
    close_count = 0

    for i in range(0, len(string)):
        if string[i] == '[':
            open_count += 1
        if string[i] == ']':
            close_count += 1
        if close_count > open_count:
            return True

    return False

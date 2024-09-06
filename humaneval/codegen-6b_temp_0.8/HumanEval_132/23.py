
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
    parsed = brackets(string)
    nest = 0
    for c in parsed:
        if c == '[' and nested == -1:
            nest += 1
        elif c == ']' and nested == -1:
            nest -= 1
        if nest < 0:
            return False
    return not nest
    
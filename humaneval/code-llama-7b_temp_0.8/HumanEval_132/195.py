
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
    #dicts = {'[':']', ']':'[', '(':')', ')':'('}
    dicts = {'[':']', ']':'[', '(':')', ')':'('}
    #check if 1. has '[' or ']' or '(' or ')'
    if ('[' in string) or (']' in string) or ('(' in string) or (')' in string):
        print("True")
    else:
        print("False")


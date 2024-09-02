
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
    lst = list(string)
    idx = 0
    while idx < len(lst):
        if lst[idx] == '[':
            lst[idx] = 0
        elif lst[idx] == ']':
            lst[idx] = 1
        idx += 1
    return 1 in lst



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
    # Create a function that takes a string as input which contains only square brackets.
    # The function should return True if and only if there is a valid subsequence of brackets 
    # where at least one bracket in the subsequence is nested.
    l = ['[',']']
    s = []
    for i in string:
        if i in l:
            s.append(i)
        else:
            s.pop()
    return True if s else False

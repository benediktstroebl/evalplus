
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
    lst = []
    for i in range(len(string)):
        if string[i] == '[':
            lst.append('left')
        else:
            if lst and lst[-1] == 'left':
                lst.pop()
            else:
                lst.append('right')
    return lst!= []


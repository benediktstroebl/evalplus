
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
    '''
    '[]'
    '[]]'
    '[[]'
    '[[]]'
    '''
    if len(string) == 0:
        return False

    lst = []
    for char in string:
        if char == '[':
            lst.append(char)
        elif char == ']':
            if len(lst) > 0 and lst[-1] == '[':
                lst.pop()
            else:
                return False

    return lst == []



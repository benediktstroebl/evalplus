
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
    if string == []: return False
    if len(string) % 2!= 0: return False
    s = []
    for i in string:
        if i == '[': s.append(']')
        elif i == ']':
            if not s: return False
            if s.pop()!= i: return False
    return not s


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
    brackets = []
    if not string:
        return False
    for i in string:
        if i == '[':
            brackets.append('[')
        elif i == ']':
            if len(brackets)!= 0:
                brackets.pop()
        elif len(brackets)!= 0 and i == '[' and brackets[-1] == '[':
            brackets.append('[')
        if len(brackets) == 0:
            return True
    return False


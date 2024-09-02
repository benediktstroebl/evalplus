
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
    open_bracket = set('[')
    close_bracket = set(']')
    stack = []
    for i in string:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            if not stack:
                return False
            elif stack.pop() == '[' and close_bracket[i]!= ']':
                return False
    return not stack



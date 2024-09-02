
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

    if not string:
        return True
    
    stack = []
    open_bracket = {'(', '['}
    close_bracket = {')': '(', ']': '['}
    
    for bracket in string:
        if bracket in open_bracket:
            stack.append(bracket)
        elif bracket in close_bracket:
            if not stack:
                return False
            if close_bracket[bracket] == stack[-1]:
                stack.pop()
    return True if not stack else False


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
    # Refer - http://www.geeksforgeeks.org/check-for-balanced-parentheses
    # (Note : The solution is not efficient, so please optimise it)
    stack = []
    for s in string:
        if s == '[':
            stack.append('[')
        elif s == ']':
            if not stack:
                return False
            if stack.pop() == '[':
                continue
            else:
                return False
    return not stack

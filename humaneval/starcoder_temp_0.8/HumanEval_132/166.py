
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
    open_bracket = '(['
    close_bracket = ')]'
    stack = []
    for i in string:
        if i in open_bracket:
            stack.append(i)
        if i in close_bracket:
            if len(stack) == 0:
                return False
            elif close_bracket.index(i) == open_bracket.index(stack[-1]):
                stack.pop()
    return len(stack)!= 0

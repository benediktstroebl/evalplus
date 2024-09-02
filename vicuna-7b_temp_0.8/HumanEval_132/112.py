
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
    stack = []
    nesting = False
    for c in string:
        if c == '[':
            stack.append(c)
            nesting = not nesting
        elif c == ']':
            if nesting:
                nesting = False
                if stack[-1] == '[':
                    nesting = True
                elif stack[-1] == ']':
                    return False
            stack.pop()
        elif c == ']':
            nesting = not nesting
    return True

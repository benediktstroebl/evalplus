
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
    brackets = '[]'
    for b in string:
        if b in brackets:
            stack.append(b)
        else:
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if b == ']' and top != '[':
                    return False
                elif b == ')' and top != '(':
                    return False
    return len(stack) == 0


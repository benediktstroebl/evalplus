
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
    s = list(string)
    stack = []
    while s:
        e = s.pop()
        if e == '[' or e == '(' or e == '{':
            stack.append(e)
        elif e == ']' or e == ')' or e == '}':
            if not stack:
                return False
            elif e == ']' and stack[-1] != '[' or e == ')' and stack[-1] != '(':
                return False
            elif e == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
    return not stack
    


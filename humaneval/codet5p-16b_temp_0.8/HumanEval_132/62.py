
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

    
    if string == "":
        return False
    
    b = [s for s in string]
    stack = []
    while len(b) > 0:
        x = b.pop(0)
        if x in '[{(':
            stack.append(x)
        elif x in ')]}':
            if len(stack) == 0:
                return False
            last = stack.pop()
            if last == '[' and x == ']':
                continue
            elif last == '{' and x == '}':
                continue
            elif last == '(' and x == ')':
                continue
            else:
                return False
    return len(stack) == 0



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

    
    def valid(sub):
        stack = []
        for c in sub:
            if c == '[' and len(stack) == 0:
                return False
            elif c == '[' and len(stack) > 0:
                stack.append(c)
            elif c == ']' and len(stack) == 0:
                return False
            elif c == ']' and len(stack) > 0:
                stack.pop()
        return len(stack) == 0
    
    return valid(string)

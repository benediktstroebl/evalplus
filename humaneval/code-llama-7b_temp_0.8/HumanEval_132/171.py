
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
    if string == '':
        return False
    else:
        stack = []
        for i in string:
            if i == '[' or i == '(':
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == '[' and i == ']':
                    stack.pop()
                elif stack[-1] == '(' and i == ')':
                    stack.pop()
                else:
                    return False
        return True

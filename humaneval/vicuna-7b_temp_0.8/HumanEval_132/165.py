
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
    nest = []
    for i in string:
        if i == '[':
            if nest:
                stack.append(nest)
                nest = []
            else:
                stack.append(i)
                nest = [i]
        elif i == ']':
            if stack:
                nest.append(stack.pop())
            else:
                nest.append(i)
        elif i == '[' and nest:
            nest.append(stack[-1])
        elif i == ']' and not nest:
            return False
        else:
            nest.append(i)

    return nest

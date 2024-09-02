
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
    stack = ['-1']
    for el in string:
        if el == '[':
            stack.append(el)
        elif el == ']':
            if stack[-1] == '-1':
                stack.pop()
            else:
                if stack[-1] == '[' or stack[-1] == '{':
                    stack.append(el)
                else:
                    return False
    return stack[-1] == '-'
    
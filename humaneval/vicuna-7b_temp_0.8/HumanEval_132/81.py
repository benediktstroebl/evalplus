
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
    for i in range(1, len(string)):
        if string[i] == '[' and string[i-1] != '\\':
            stack.append(string[i-1])
        elif string[i] == ']' and string[i-1] != '\\':
            if stack[-1] == '\\':
                stack.pop()
            else:
                if stack[-1] == '[':
                    return True
                else:
                    return False
    return False
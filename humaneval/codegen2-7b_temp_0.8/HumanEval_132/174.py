
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
    for i in range(len(s)):
        if s[i] == '[':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                if s[i] == ']' and s[i - 1] == '[' and stack.pop() == '[':
                    continue
                else:
                    return False
    return len(stack)


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
    for ch in string:
        if ch == '[':
            stack.append(ch)
        elif ch == ']':
            if stack:
                if stack[-1] == '[' and stack[-2] == ']':
                    # nested bracket
                    return True
                else:
                    # not a valid subsequence
                    return False
            stack.pop()
    return not stack

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
    if '[' in string:
        stack = []
        for i in string:
            if i == '[' and not stack:
                stack.append(i)
            elif i == '[' and stack:
                stack.pop()
            elif i == ']' and stack:
                stack.pop()
            elif i == ']' and not stack:
                return False
        return True
    else:
        return

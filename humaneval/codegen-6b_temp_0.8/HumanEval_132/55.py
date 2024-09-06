
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
    if len(string) <= 2:
        return False

    if len(string) == 3 and string[0] == '[' and string[-1] == ']':
        return True

    if len(string) == 3:
        return string[1] == '['

    stack = []
    for item in string:
        if item == '[':
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            if item == ']' and stack[-1] != '[':
                return False
            if item == ']' and stack[-1] == '[':
                stack.pop()
    return False

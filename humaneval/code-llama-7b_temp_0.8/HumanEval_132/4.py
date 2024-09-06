
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
    arr = list(string)
    if arr[0] != '[' or arr[-1] != ']':
        return False

    stack = []
    for i in range(0, len(arr)):
        if arr[i] == '[':
            stack.append(i)
        if arr[i] == ']':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


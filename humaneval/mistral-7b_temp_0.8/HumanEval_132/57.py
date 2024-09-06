
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
    brackets = []
    for i in range(len(arr)):
        if arr[i] == '[':
            brackets.append('[')
        elif arr[i] == ']':
            brackets.append(']')
        if arr[i] == '[' and arr[i+1] == '[':
            return True
    if len(brackets) % 2 != 0:
        return False
    for i in range(len(brackets)):
        if brackets[i] == '[' and brackets[i+1] == ']':
            brackets[i] = ']'
            brackets[i+1] = '['
    if len(brackets) != 1:
        return False
    elif len(brackets) == 1:
        if brackets[0] == ']' and brackets[1] == '[':
            return True
        else:
            return False
    return False


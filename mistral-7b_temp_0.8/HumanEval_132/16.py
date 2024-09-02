
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
    array = string.split("]")
    array.append("]")
    stack = []

    for i in range(len(array)):
        if array[i] == "[":
            stack.append(array[i])
        elif array[i] == "]":
            if len(stack) > 0:
                if array[i] == stack[0]:
                    stack.pop(0)
    return len(stack) != 0


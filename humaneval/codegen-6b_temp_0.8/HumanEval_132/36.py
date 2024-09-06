
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
    # your code here
    ##
    # solve the recursive case
    # if string[left] == '[' and string[right] == ']':
    #     return is_nested(string[1:right + 1]) and is_nested(string[right + 1:])
    # else:
    #     return False

    ##
    # solve the iterative case
    stack = []

    for char in string:
        if char == '[' and len(stack) > 0:
            stack.pop()
        elif char == ']' and len(stack) == 0:
            return False
        else:
            stack.append(char)

    return len(stack) == 0


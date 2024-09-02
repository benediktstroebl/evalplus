
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
    if len(string)<3:
        return False

    open_bracket = '['
    close_bracket = ']'

    stack = []

    for i in range(0,len(string)):
        if string[i] == open_bracket:
            stack.append(i)

        elif string[i] == close_bracket:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True

    return False

    # Solution 2
    # stack = []
    # for i in string:
    #     if i == '[':
    #         stack.append(i)
    #     elif i == ']':
    #         if len(stack) == 0:
    #             return False
    #         stack.pop()
    # return True if len(stack) == 0 else False



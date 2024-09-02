
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

    # stack = 0
    # for i in string:
    #     if i == '[':
    #         stack += 1
    #     if i == ']':
    #         stack -= 1
    #     if stack < 0:
    #         return True
    # return False

    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if stack:
                stack.pop()
            else:
                return True
    return False

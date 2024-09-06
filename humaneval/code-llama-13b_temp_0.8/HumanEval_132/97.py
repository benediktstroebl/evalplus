
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
    # array = []
    # for i in string:
    #     array.append(i)

    # array.pop(0)
    # array.pop(-1)
    # stack = []
    # for i in array:
    #     if i == '[':
    #         stack.append(i)
    #     elif i == ']':
    #         stack.pop()
    # return (len(stack) > 0)
    # return (string.count('[') != string.count(']'))
    return string.count('[') != string.count(']')


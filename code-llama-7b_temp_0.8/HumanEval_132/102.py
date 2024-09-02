
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
    # nested = []
    # for i, letter in enumerate(string):
    #     if letter == '[':
    #         nested.append(i)
    #     elif letter == ']' and nested:
    #         nested.pop()
    #     elif letter == ']' and not nested:
    #         return True
    # return False

    nested = []
    for i, letter in enumerate(string):
        if letter == '[':
            nested.append(i)
        elif letter == ']' and nested:
            nested.pop()
    if nested:
        return True
    else:
        return False


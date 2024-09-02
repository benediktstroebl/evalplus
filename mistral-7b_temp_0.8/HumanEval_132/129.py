
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

    result = False
    index = 0

    while index < len(string):

        if string[index] == '[':
            if string[index + 1] == '[':
                result = True
                break
            if string[index + 1] == ']':
                break

        if string[index] == ']':
            if string[index - 1] == '[':
                result = True
                break
            if string[index - 1] == ']':
                break

        index += 1

    return result


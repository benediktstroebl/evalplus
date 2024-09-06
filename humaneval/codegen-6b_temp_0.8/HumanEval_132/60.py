
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
    if string[0] is not '[':
        return False

    if string[-1] is not ']':
        return False

    if len(string) <= 2:
        return False

    if string.count('[') != string.count(']'):
        return False

    if string.count('[') != string.count(']'):
        return False

    if string.count('[') == 0 or string.count(']') == 1:
        # only need to look for the nested brackets
        return is_nested(string[1:-1])

    # if we got here, then we have found a nested sub-segment of brackets, now we need to check
    # for any other nested brackets in the sub-string
    to_return = False
    counter = 0
    for i in range(1, len(string)):
        if string[i] == '[':
            counter += 1

        if string[i] == ']':
            counter -= 1
            if counter < 0:
                return False

    if counter != 0:
        return False

    return to_return


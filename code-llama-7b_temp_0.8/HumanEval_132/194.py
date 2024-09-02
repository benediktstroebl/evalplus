
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
    # create variables
    count1, count2 = 0, 0

    # loop over string
    for char in string:
        if char == '[':
            count1 += 1
        elif char == ']':
            count2 += 1

        if count1 == count2 and count1 != 0 and count2 != 0:
            return True

    return False


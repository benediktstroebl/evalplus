
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
    square_brackets = []
    for x in string:
        if x == '[':
            square_brackets.append('[')
        else:
            square_brackets.append(']')
    for x in square_brackets:
        if square_brackets.count(x) > 1 and square_brackets.count(x) % 2 == 1:
            result = True
    return result

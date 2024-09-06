
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
    string = list(string)
    bracket = '['
    closed_bracket = ']'
    left_brackets = 0
    right_brackets = 0

    for c in string:
        if c == bracket:
            left_brackets += 1
        elif c == closed_bracket:
            right_brackets += 1

        if right_brackets > left_brackets:
            return False

    return True


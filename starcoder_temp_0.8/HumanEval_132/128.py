
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
    brackets = list(string)

    while len(brackets) > 1:
        if brackets[0] == '[' and brackets[-1] == ']':
            brackets.pop(0)
            brackets.pop()
        else:
            return False

    if len(brackets) == 1:
        return brackets[0] == ']'

    return False

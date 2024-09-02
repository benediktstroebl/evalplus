
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

    open_bracket = '['
    close_bracket = ']'

    if len(string) % 2 != 0:
        return False

    brackets = []

    for symbol in string:
        if symbol == open_bracket:
            brackets.append(open_bracket)
        elif symbol == close_bracket:
            if brackets:
                if brackets[-1] == open_bracket:
                    brackets.pop()
                else:
                    brackets.append(close_bracket)
            else:
                brackets.append(close_bracket)

    return bool(brackets)



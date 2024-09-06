
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
    brackets = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    unclosed = []
    for bracket in string:
        if bracket in brackets:
            unclosed.append(brackets[bracket])
        else:
            if not unclosed:
                return False
            unclosed.pop()
    return not unclosed

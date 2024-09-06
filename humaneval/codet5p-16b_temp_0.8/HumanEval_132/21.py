
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

    open_brackets = '['
    closed_brackets = ']'
    brackets = []
    for bracket in string:
        if bracket in open_brackets:
            brackets.append(bracket)
        else:
            if not brackets or closed_brackets!= bracket:
                return False
            else:
                brackets.pop()
    if brackets:
        return False
    else:
        return True


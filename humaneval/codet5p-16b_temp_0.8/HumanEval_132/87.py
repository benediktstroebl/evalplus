
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

    open_brackets = "([{"
    closed_brackets = ")]}"
    brackets = []

    for char in string:
        if char in open_brackets:
            brackets.append(char)
        elif char in closed_brackets:
            if not brackets:
                return False
            if closed_brackets.index(char)!= open_brackets.index(brackets[-1]):
                return False
            brackets.pop()
    return False if brackets else True


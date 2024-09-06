
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
    if string == "":
        return False
    check = False
    bracket = []
    for s in string:
        if s == "[":
            bracket.append(s)
        elif s == "]":
            if len(bracket) == 0:
                return False
            else:
                bracket.pop()
    return False if len(bracket) != 0 else True
​
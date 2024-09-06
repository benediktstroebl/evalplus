
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
    open = 0
    close = 0
    for i in string:
        if i == "[" and open == 0:
            open += 1
        if i == "]" and open > 0:
            open -= 1
        if open < 0:
            return True
        if open == 0 and i == "]":
            close += 1
        if open == 0 and i == "[":
            return False
    return close > 0

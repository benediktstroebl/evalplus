
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
    opening = 0
    closing = 0
    for i in string:
        if i == "[":
            opening += 1
        elif i == "]":
            closing += 1
            if closing > opening:
                return False
    return True if closing != 0 and closing == opening else False
    

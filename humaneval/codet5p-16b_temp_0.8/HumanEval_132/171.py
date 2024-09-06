
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

    
    brackets = []
    for char in string:
        if char == '[':
            brackets.append(']')
        elif char == ']' and len(brackets) > 0 and brackets[-1] == '[':
            brackets.pop()
        else:
            return False

    return True if len(brackets) == 0 else False

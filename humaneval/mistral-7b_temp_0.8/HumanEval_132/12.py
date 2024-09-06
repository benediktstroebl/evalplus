
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
    is_nested = []
    for char in string:
        if char == "[":
            is_nested.append("(")
        elif char == "]":
            if len(is_nested) == 0:
                is_nested.append("]")
            else:
                is_nested.pop()
    return True if len(is_nested) == 0 else False



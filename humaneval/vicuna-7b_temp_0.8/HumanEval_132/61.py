
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
    for char in string:
        if char == "[":
            if string[0] == "[":
                return True
        elif char == "]":
            if string[0] == "[" and string[-1] == "]":
                return True
        elif char == "]":
            if string[0] == "[" and string[1:3] == ["[", "]"]:
                return True
        elif char == "[":
            if string[0] == "[" and string[-1] == "]":
                return True
        elif char == "]":
            if string[0] == "[" and string[1:3] == ["[", "]"]:
                return True
        elif char == "]":
            if string[0] == "[" and string[1:5] == ["[", "]"]:
                return True
    return False
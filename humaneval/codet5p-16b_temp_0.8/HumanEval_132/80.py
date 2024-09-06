
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

    bracket_stack = []
    bracket_dict = {"]":"[", "}":"{", ")":"("}
    
    for char in string:
        if char in bracket_dict.values():
            bracket_stack.append(char)
        elif char in bracket_dict.keys():
            if bracket_dict[char] == bracket_stack[-1]:
                bracket_stack.pop()
            else:
                return False
    return bracket_stack == []


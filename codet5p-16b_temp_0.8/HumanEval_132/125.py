
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
    bracket_map = {']': '[', ')': '(', '}': '{'}
    
    for character in string:
        if character in bracket_map.values():
            bracket_stack.append(character)
        elif character in bracket_map:
            if bracket_map[character] == bracket_stack.pop():
                continue
            else:
                return False

    return not bracket_stack

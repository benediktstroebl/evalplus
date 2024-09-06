
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
    bracket_dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    for bracket in string:
        if bracket in bracket_dict:
            bracket_stack.append(bracket)
        else:
            if bracket_stack:
                if bracket_dict[bracket_stack[-1]] == bracket:
                    bracket_stack.pop()
                else:
                    return False
            else:
                return False
    return bracket_stack == []

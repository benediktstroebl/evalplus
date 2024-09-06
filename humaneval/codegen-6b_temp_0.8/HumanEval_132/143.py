
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
    valid_brackets = {'(':')', '[':']', '{':'}'}
    stack = []
    for bracket in string:
        if bracket in valid_brackets:
            stack.append(bracket)
        elif stack and valid_brackets[stack[-1]] == bracket:
            stack.pop()
        else:
            return False

    return len(stack) == 0

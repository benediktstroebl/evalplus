
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
    length = len(string)
    if length <= 1:
        return False

    opening_bracket = -1
    closing_bracket = -1
    current_bracket = -1
    isNested = False
    stack = []

    for i in range(length):
        if string[i] == '[':
            new_bracket = i
            if not stack:
                current_bracket = new_bracket
            stack.append(new_bracket)
        elif string[i] == ']':
            stack.pop()
            if not stack:
                current_bracket = new_bracket
                opening_bracket = i
            else:
                current_bracket = stack[-1]

        if i == length - 1:
            if not stack:
                isNested = True
            else:
                isNested = False

    return isNested


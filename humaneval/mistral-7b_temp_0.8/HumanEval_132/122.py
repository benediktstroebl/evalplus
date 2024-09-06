
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
    stack = []

    for character in string:
        if character == '[':
            stack.append(character)
        elif character == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

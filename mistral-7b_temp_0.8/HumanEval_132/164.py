
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

    '''
    The function will loop through the string, and if we find a ']' character, we will pop the
    last '[' character off the stack. If we cannot pop it off the stack, that means the last '['
    character is not nested, so we return False. Otherwise, we continue with the next character.
    '''
    stack = []
    for char in string:
        if char == ']':
            if not stack:
                return False
            stack.pop()
        elif char == '[':
            stack.append(char)
    return True

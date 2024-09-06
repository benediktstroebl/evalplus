
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
    # my solution
    brackets = string.replace('[','').replace(']','')
    is_balanced = True
    for char in brackets:
        if char == '(':
            is_balanced = not is_balanced
        if char == ')' and is_balanced == False:
            return False
    return True

    # solution 1
    stack = []
    for ch in string:
        if ch in '[]':
            stack.append(ch)
        else:
            if stack[-1] == ch:
                stack.pop()
            else:
                return False
    return not stack

    # solution 2
    if len(string) % 2 == 1:
        return False
    string = ''.join(string.split(']')[::-1])
    return '[' in string and '[' not in string

    # solution 3
    return '][' in string

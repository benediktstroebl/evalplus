
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
    substr_stack = []
    for char in string:
        if char == '[' and substr_stack and substr_stack[-1]!= '[':
            substr_stack.append(char)
        elif char == ']':
            if not substr_stack or substr_stack[-1] == '[':
                return False
            substr_stack.pop()
    return not substr_stack
    


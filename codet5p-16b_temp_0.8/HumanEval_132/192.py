
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
    left = "([{"
    right = ")]}"
    for char in string:
        if char in left:
            stack.append(char)
        elif char in right:
            if not stack or left.find(stack.pop())!= right.find(char):
                return False
    return not stack
    

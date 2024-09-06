
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
    # utilize stack data structure and while loop to traverse the input string
    stack = []
    # traverse the input string
    for ch in string:
        if ch == '[':
            stack.append(ch)
        elif ch == ']':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return False if stack else True

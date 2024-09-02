
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
    # Make a dict that associates top level brackets with the indices of their respective
    # nested brackets
    nested_dict = {}
    stack = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(c)
        elif c == ']':
            if not stack:
                return False
            nested_dict[stack[-1]] = i
            stack.pop(-1)

    # If stack is not empty, the brackets are not nested, as there's no corresponding closing bracket.
    return len(stack) == 0



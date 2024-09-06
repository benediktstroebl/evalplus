
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
    # nested_brackets = ['()', '[]', '{}', '<>']
    # brackets = nested_brackets + [x + y for x in nested_brackets for y in nested_brackets]
    brackets = '()[]<>{}[]'
    stack = []
    for b in string:
        if b in brackets:
            stack.append(b)
        elif len(stack) == 0 or stack.pop() != b:
            return False
    if len(stack) == 0:
        return True
    return False


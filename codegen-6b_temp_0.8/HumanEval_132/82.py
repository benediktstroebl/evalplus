
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
    open_brackets = ['[', '{', '(']
    close_brackets = [']', '}', ')']
    stack = []
    for c in string:
        if c in open_brackets:
            stack.append(c)
        elif c in close_brackets:
            if len(stack) == 0:
                return False
            else:
                if c == close_brackets[close_brackets.index(stack.pop())]:
                    continue
                return False
    return len(stack) == 0

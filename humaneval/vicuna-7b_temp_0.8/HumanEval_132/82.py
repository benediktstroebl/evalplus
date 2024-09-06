
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
    curr = string[0]
    for ch in string:
        if ch == curr[0]:
            stack.append(ch)
        else:
            if len(stack) > 0:
                # push the top of stack to the curr
                curr.append(stack.pop(0))
                # reset the stack
                stack = [ch]
            # curr is not a bracket
            curr = ch
        if curr == ']':
            # push the top of stack to the curr
            curr.append(stack.pop(0))
            # reset the stack
            stack = [ch]
    return True
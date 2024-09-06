
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
    

    def valid(stack):
        while stack:
            top = stack.pop()
            if not stack and top != "[":
                return False
            elif top == "]" and stack.pop() != "[":
                return False
            elif top == "]" and stack.pop() == "[":
                return False
        return True

    stack = []
    for i, ch in enumerate(string):
        if ch == "[":
            stack.append(ch)
        else:
            if len(stack):
                stack.pop()
            else:
                return False
    return True

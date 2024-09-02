
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
    def is_nested_1(string):
        if len(string) <= 0:
            return False
        stack = []
        for c in string:
            if c == ']':
                if len(stack) == 0 or stack[-1] == '[':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
    def is_nested_2(string):
        stack = []
        for c in string:
            if c == '[' or c == ']':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                index_top = len(stack) - 1
                if stack[index_top] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    if is_nested_1(string):
        return True
    else:
        return is_nested_2(string)


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
    def is_valid_nested(string):
        stack = []
        for c in string:
            if c == '[':
                stack.append(c)
            elif c == ']':
                if len(stack) == 0 or stack[-1]!= '[':
                    return False
                stack.pop()
        return len(stack) == 0
    return is_valid_nested(string)


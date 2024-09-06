
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
    # ~ O(n) Time Complexity
    def is_balanced(string):
        if not string:
            return True
        if string[0] != '[' and string[-1] != ']':
            return False
        return is_balanced(string[1:-1])
    
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
    return is_balanced(stack)

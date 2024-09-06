
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
    if not string:
        return False
    else:
        string_len = len(string)
        # initialise the stack
        stack = []
        # loop through the string
        for i in range(string_len):
            # check if the current character is a left bracket
            if string[i] == '[':
                # push the current character into the stack
                stack.append('[')
            # check if the current character is a right bracket
            elif string[i] == ']':
                # if the stack is not empty, pop the top element
                # if the popped element is a left bracket, it means that the right bracket is not paired correctly
                if stack:
                    if stack[-1] == '[':
                        return False
                    stack.pop()
        return True if stack else False




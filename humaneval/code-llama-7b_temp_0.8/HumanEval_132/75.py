
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
    # the stack to store bracket index
    stack = []

    # the dict to map bracket to index
    dict_bracket = {}

    # loop the string
    for i, s in enumerate(string):
        # if find a closing bracket
        if s == ']':
            # if the stack is not empty
            if stack:
                # check the top of stack
                if string[stack[-1]] == '[':
                    # check whether the brackets are nested
                    if stack[-1] < i - 1:
                        return True
                    else:
                        stack.pop()

        # if find a opening bracket
        elif s == '[':
            # push the index into stack
            stack.append(i)

    # if there is no nested bracket
    return False

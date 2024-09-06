
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
    # non-empty strings only contain square brackets
    if len(string) > 1:
        # list that contains opening brackets
        stack = []
        # for every char in string
        for char in string:
            # if there is an open bracket
            if char == '[':
                # append to stack
                stack.append(char)
            # else (there is a closing bracket)
            else:
                # if the stack is not empty
                if stack:
                    # pop the last element from the stack
                    stack.pop()
                # else (the stack is empty)
                else:
                    # return False
                    return False
        # if the stack is empty after looping through the string
        if not stack:
            # return True
            return True
        # else (the stack is not empty)
        else:
            # return False
            return False
    # else (the string is empty or has only one char)
    else:
        # return False
        return False


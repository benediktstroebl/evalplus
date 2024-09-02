
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
    # initializing empty stack and s
    s, stack = [], []
    # iterating over string
    for i in string:
        # if it is a closing bracket
        if i == "]":
            # check if stack is empty
            if not stack:
                return False
            # if stack is not empty
            else:
                # pop and append stack to s
                s.append(stack.pop())
        # if it is a opening bracket
        else:
            # push it to stack
            stack.append(i)
    # after iterating
    # check if stack is empty
    if stack:
        return False
    # if stack is not empty
    else:
        # if length of s is more than 1
        if len(s) > 1:
            # return true
            return True
        # if length of s is equal to 1
        elif len(s) == 1:
            # return false
            return False


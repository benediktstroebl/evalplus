
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
    # return string.count(']') > 0
    
    # valid = False
    # stack = []
    
    # for char in string:
    #     if char == '[':
    #         stack.append(char)
    #     else:
    #         if len(stack) == 0:
    #             continue
    #         else:
    #             stack.pop()
    #             if not stack:
    #                 valid = True
            
    # return valid
    
    valid = False
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        else:
            if len(stack) == 0:
                continue
            else:
                stack.pop()
                if stack:
                    valid = True
                    
    return valid


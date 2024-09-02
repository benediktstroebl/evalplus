
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
    # My solution
    # result = False
    # flag = 0
    # for i in range(len(string)):
    #     if string[i] == "[" and flag <= 0:
    #         flag += 1
    #     elif string[i] == "]" and flag >= 1:
    #         flag -= 1
    #     elif string[i] == "]" and flag == 0:
    #         result = True
    # return result

    # Kin's solution
    if string:
        stack = []
        for i in range(len(string)):
            if string[i] == '[':
                stack.append(i)
            if string[i] == ']':
                if not stack:
                    return True
                stack.pop()
        return False


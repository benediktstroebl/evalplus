
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
    balanced = []
    for i in string:
        if i == '[':
            balanced.append('[')
        elif i == ']':
            if len(balanced) == 0:
                return False
            else:
                balanced.pop()
    return True if len(balanced) > 0 else False

    # for i in range(len(string)):
    #     if string[i] == '[':
    #         nested = 0
    #         for j in range(i+1,len(string)):
    #             if string[j] == ']':
    #                 nested += 1
    #             if nested == 2:
    #                 return True






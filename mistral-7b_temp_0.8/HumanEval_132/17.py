
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
    #solution:
    # string = '['
    # for i in range(len(string)):
    #     if string[i] == '[' and string[i+1] == '[':
    #         print(True)
    #         break
    # else:
    #     print(False)

    string = '['
    if string[0] == '[':
        return False
    elif string[1] == ']':
        return False
    else:
        return True

    # string = '['
    # if string[0] == '[' and string[len(string)-1] == ']':
    #     return True
    # else:
    #     return False


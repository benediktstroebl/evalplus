
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
    # for i in range(int(len(string)/2)):
    #     if string[i] == "]" and string[-1-i] == "[":
    #         return True
    #     elif string[i] == ")" and string[-1-i] == "(":
    #         return True
    #     else:
    #         return False
    

    if string == "":
        return True
    elif string[0] == "[" and string[-1] == "]":
        return True
    elif string[0] == "{" and string[-1] == "}":
        return True
    else:
        return False

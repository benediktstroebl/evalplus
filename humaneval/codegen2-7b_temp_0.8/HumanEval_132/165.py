
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
    if string[0] == '[' and string[-1] == ']':
        return True
    if string[0] == '[' and string[1]!= ']':
        for i in range(2,len(string)-1):
            if string[i] == '[':
                if string[i-1] == ']':
                    if is_nested(string[i+1:]) == True:
                        return True
                if string[i+1] == '[' and string[i+2] == ']':
                    if is_nested(string[i+3:]) == True:
                        return True
        return False

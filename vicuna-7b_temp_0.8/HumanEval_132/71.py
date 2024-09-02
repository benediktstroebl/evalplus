
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
    if '[]' in string:
        nested = 0
        for i in range(len(string)):
            if string[i:i+2] == '[]':
                nested += 1
            elif string[i:i+2] == ']':
                if nested > 0:
                    return True
                nested = 0
            elif string[i:i+2] == '(':
                nested += 1
            elif string[i:i+2] == ')':
                if nested > 0:
                    return True
                nested = 0
            elif string[i:i+1] == '[':
                nested += 1
            elif string[i:i+1] == ']':
                nested -= 1
        if nested > 0:
            return True
        return False
    else:
        return False

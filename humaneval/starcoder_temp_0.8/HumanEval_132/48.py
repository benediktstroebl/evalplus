
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
    if string.count('[')!= string.count(']'):
        return False
    for i in range(len(string)):
        if string[i] == '[' and string[i+1]!= ']':
            j = i+1
            while j < len(string):
                if string[j] == '[':
                    j += 1
                elif string[j] == ']':
                    break
                elif j+1 < len(string) and string[j+1] == '[':
                    return True
                elif j+1 < len(string) and string[j+1] == ']':
                    return False
                j += 1
        elif string[i] == '[' and string[i+1] == ']':
            return True
    return False


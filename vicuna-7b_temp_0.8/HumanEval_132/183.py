
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
    for char in string:
        if char == '[':
            for i in range(1, len(string)):
                if string[i] == '[' and string[i+1] == char:
                    nested = True
                    for j in range(i+2, len(string)):
                        if string[j] == ']' and string[j-1] == char:
                            nested = False
                            break
                    if nested:
                        return True
                    i += 1
        elif char == ']':
            nested = False
            for i in range(0, len(string)-1):
                if string[i] == '[' and string[i+1] == char:
                    nested = True
                    break
                if string[i] == ']' and string[i+1] == char:
                    nested = False
                    break
            if nested:
                return True
    return False

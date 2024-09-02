
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
    if string == '':
        return True
    i = 0
    while i < len(string):
        if string[i] == '[':
            count = 0
            while string[i] == '[':
                count += 1
                i += 1
            if string[i] == ']':
                i += 1
                while count > 0 and i < len(string):
                    if string[i] == ']':
                        count -= 1
                        i += 1
                    if string[i] == '[':
                        count += 1
                        i += 1
                if count == 0:
                    return True
            else:
                return False
        else:
            return False
    return True


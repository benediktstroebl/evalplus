
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

    if string == []:
        return False
    elif string == ['[', ']']:
        return False
    elif string[0] == ']':
        return False
    elif string[-1] == '[':
        return False
    elif string[0] == '[' and string[-1] == ']':
        return True

    else:
        temp = []
        for i in range(len(string)):
            if string[i] == '[':
                temp.append(string[i])
            elif string[i] == ']':
                if len(temp) == 0:
                    return False
                else:
                    temp.pop()
        return False if len(temp) > 0 else True

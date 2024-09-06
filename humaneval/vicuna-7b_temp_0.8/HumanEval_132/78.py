
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
    nested = []
    for i in range(len(string)):
        if string[i] == '[' and string[i+1] == '[':
            nested.append(string[i+1])
            i += 2
        elif string[i] == ']' and string[i-1] == '[':
            nested.append(string[i-1])
            i -= 2
    for b in nested:
        for j in range(len(nested)):
            if j != i:
                if string[i+1] == ']' and string[j] == '[':
                    return True
            elif j == i and string[i-1] == ']':
                return True
    return False
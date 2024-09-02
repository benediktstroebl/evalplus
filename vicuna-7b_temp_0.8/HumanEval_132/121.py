
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
    string = ''.join(sorted(string))
    nested = []
    for i in range(len(string)):
        if string[i:i+2] == '[]':
            nested.append(i)
            for j in range(i+2, len(string)):
                if string[j:j+2] == '[]':
                    nested.append(j)
    return len(nested) > 0

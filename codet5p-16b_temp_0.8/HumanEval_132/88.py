
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
        return False
    brackets = []
    for i in range(len(string)):
        if string[i] == '[':
            brackets.append(string[i])
        if string[i] == ']':
            if len(brackets)!= 0:
                brackets.pop()
            else:
                return False
    if len(brackets) == 0:
        return True
    else:
        return False



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
    string = string.replace('[]', '')
    i = 0
    j = 1
    brackets = list(string)
    while i < len(brackets):
        if brackets[i] == '[' and brackets[j] == ']':
            brackets[j] = '*'
            j += 1
        i += 1
    if '*' in brackets:
        return True
    else:
        return False


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
    nested_brackets = 0
    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        elif string[i] == ']':
            nested_brackets += 1
        if count == nested_brackets:
            break
    return count > nested_brackets


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
    # Your implementation goes here
    if len(string) == 0:
        return True
    if len(string) == 1:
        return string.startswith('[')
    nesting = 0
    start = 0
    for i in range(1, len(string)):
        if string[i:i+2] == '[]' and string[start:i] == '[':
            nesting += 1
            start = i + 1
        elif string[i:i+2] == ']' and string[start:i] == '[':
            nesting -= 1
            if nesting < 0:
                return False
        elif string[i:i+2] != '[]':
            start = i+1
    return nesting > 0

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
    if len(string) == 0 or len(string) == 1:
        return False

    substrings = []
    for i in range(1,len(string)):
        substrings.append(string[i-1:i+1])
    print(substrings)
    
    for substring in substrings:
        if substring == '[]':
            return True
    return False
    


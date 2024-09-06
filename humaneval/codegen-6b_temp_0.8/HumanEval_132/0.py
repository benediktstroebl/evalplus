
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
    
    extracted = extract_brackets(string)
    count = 0
    for s in extracted:
        if s == '}' or s == ']':
            count += 1
    return count > 1
    
    #return count([s for s in extracted if s == '}' or s == ']']) > 1

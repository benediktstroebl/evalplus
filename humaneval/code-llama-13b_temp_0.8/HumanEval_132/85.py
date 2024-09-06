
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
    # We could do this with a stack, but we can also use the fact that any string that is balanced,
    # has an even count of each bracket. So we can do a count of each bracket in the string and if
    # the count is even, it means that each bracket is balanced.
    
    # count opening bracket
    opening = 0
    # count closing bracket
    closing = 0
    # loop over string
    for i in string:
        # check if current character is '['
        if i == '[':
            # increment opening count
            opening += 1
        # check if current character is ']'
        if i == ']':
            # increment closing count
            closing += 1
    # return True if both counts are even
    return opening % 2 == 0 and closing % 2 == 0
    
    

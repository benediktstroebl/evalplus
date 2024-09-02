
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
    
    #Start with a count of 0 and iterate through the input string, adding 1 for every open bracket and subtracting 1 for every close bracket. When the count is 0, that means there were an even number of brackets that must be closed before another open bracket could be encountered.
    count = 0
    for i in string:
        if i == '[':
            count += 1
        elif i == ']':
            count -= 1
        if count == 0:
            return True
    return False



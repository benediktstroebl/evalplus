
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
    #initilize a counter
    counter = 0
    #loop through the string
    for char in string:
        #if its a ']' and the counter is 0, return False
        if char == ']' and counter == 0:
            return False
        #if its a '[' increase the counter
        if char == '[':
            counter += 1
        #if its a ']' decrease the counter
        if char == ']':
            counter -= 1
    #return False if the counter is not 0 at the end
    if counter != 0:
        return False
    #return True
    return True

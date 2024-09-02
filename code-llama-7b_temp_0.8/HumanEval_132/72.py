
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
    #repeat the string
    #create a list to put the paranthesis in
    #if the length of the list is not even then it will return false
    #return true
    #and if the len is even but the last element of the list is not zero
    #that will return false too
    return (
        string.count('[') == string.count(']') and 
        (string.count('[') == 0 or 
        string.count('[') % 2 == 0 and string[-1] != ']')
    )



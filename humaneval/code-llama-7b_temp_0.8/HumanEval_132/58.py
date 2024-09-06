
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
    #create a counter to count the number of brackets 
    counter = 0 
    #create a boolean to check if the bracket is nested
    nested = False
    #check if brackets are nested in the string 
    for i in range(0,len(string)):
        if string[i] == '[':
            counter += 1 
        elif string[i] == ']':
            if counter > 0:
                counter -= 1
                nested = True
            else:
                return False 
    return nested 


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
    # Loop over the string
    # If the character is a bracket and the previous bracket is not the same, add a 1 to the count
    # If the character is a bracket and the previous bracket is the same, subtract a 1 from the count
    # If the count is ever negative, return False
    # If the count is ever 0 and the previous bracket is not the same as the current bracket, return True
    # Otherwise, return False
    for i in range(1, len(string)):
        if (string[i] == ']' and string[i - 1] != ']') or (string[i] == '[' and string[i - 1] != '['):
            return False
        elif (string[i] == ']' and string[i - 1] == ']'):
            count -= 1
            if count < 0:
                return False
        elif (string[i] == '[' and string[i - 1] == '['):
            count += 1
    if count == 0:
        return True
    else:
        return False

    

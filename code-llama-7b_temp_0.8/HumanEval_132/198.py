
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
    #return False if the string is not valid
    if string[0] != '[' or string[-1] != ']': return False

    #initialize empty string
    curr_string = ''
    #initialize empty list
    list_string = []
    #loop through the input string, character by character
    for char in string:
        if char == '[': list_string.append(curr_string)
        curr_string += char
        if char == ']': curr_string = list_string.pop()
    return curr_string != ''

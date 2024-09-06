
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
    #pass
    #hint: See the notes above
    #pass
    first_bar = string.find('[')
    if first_bar == -1:
        return False
    if string.find(']') == -1:
        return True
    else:
        substrings = string.split('[')
        if [x for x in substrings if x.find(']') != -1]:
            return True
        return False



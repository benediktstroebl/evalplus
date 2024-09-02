
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
    
    if len(string) % 2!= 0:
        return False

    open_list = []
    close_list = []
    for letter in string:
        if letter == '[':
            open_list.append(letter)
        elif letter == ']':
            close_list.append(letter)
        if len(open_list)!= len(close_list):
            return False
    if open_list:
        return True
    else:
        return False



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
    if string[0] == ']': return False
    
    list_of_opening = list(string.count('['))
    list_of_closing = list(string.count(']'))
    list_of_closing.reverse()
    
    i = 0
    while i < len(list_of_closing):
        if list_of_closing[i] == 0 and i == len(list_of_closing) - 1:
            return False
        elif list_of_closing[i] == 0:
            return True
        elif list_of_closing[i] != 0 and list_of_opening[i] >= list_of_closing[i]:
            list_of_opening[i] -= list_of_closing[i]
        i += 1

    














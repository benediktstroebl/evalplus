
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
    open_bracket = '['
    close_bracket = ']'
    i = 0
    list_of_brackets = []
    while i < len(string):
        if string[i] == open_bracket:
            list_of_brackets.append(i)
        elif string[i] == close_bracket:
            list_of_brackets.append(i)
        i += 1
    open_indices = []
    close_indices = []
    for index in list_of_brackets:
        if list_of_brackets[index] == '[':
            open_indices.append(index)
        else:
            close_indices.append(index)
    for i in open_indices:
        for j in close_indices:
            if i < j:
                return True
    return False


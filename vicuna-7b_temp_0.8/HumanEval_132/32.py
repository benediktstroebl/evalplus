
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
    # The function will iterate through each character in the string
    for i, c in enumerate(string):
        # If the current character is a '[', add it to a list
        if c == '[':
            nested_list.append(c)

        # If the current character is a ']' and the list is not empty,
        # append the current character to the nested list
        if c == ']' and nested_list:
            nested_list.append(c)

        # If the current character is not a '[' or ']' and the list is not empty,
        # the nested sequence is not valid
        elif c not in ['[', ']'] and nested_list:
            return False

    # If the function has reached the end of the string without finding any brackets in the nested list,
    # return False
    return False


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

    # List of open brackets
    open_brackets = ['[', '(']

    # List of closed brackets
    closed_brackets = [']', ')']

    # List of open brackets that are also closed brackets
    pair_brackets = {'(':')', '[':']'}

    # Stores the list of open brackets that we have encountered so far
    open_brackets_list = []

    # Iterate through each character in the string
    for character in string:
        # If character is an open bracket, append it to the list of open brackets
        if character in open_brackets:
            open_brackets_list.append(character)
        # If character is a closed bracket, check that the last open bracket is a matching pair
        elif character in closed_brackets:
            last_open_bracket = open_brackets_list.pop()
            if last_open_bracket not in pair_brackets:
                return False
            elif pair_brackets[last_open_bracket]!= character:
                return False
    # Return whether there are any open brackets left
    if open_brackets_list:
        return False
    else:
        return True

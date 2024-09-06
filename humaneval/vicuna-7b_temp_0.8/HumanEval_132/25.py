
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
    # Initialize an empty string to store the current state of the brackets
    current_state = ''

    # Iterate through the string using a for loop
    for char in string:
        # If the current character is a left bracket, append it to the current state and move to the next character
        if char == '[':
            current_state += char
            continue

        # If the current character is a right bracket or the end of the string is reached, return True
        elif char == ']' or char == '':
            return True

        # If the current character is a left bracket and the previous character is the same as the current character, append the current character to the current state
        elif char == current_state[-1] and char != '\\':
            current_state += char

        # If the current character is a right bracket, append it to the current state and update the previous character
        elif char == ']':
            current_state += char
            current_state = current_state[:-1]

    # If none of the above conditions are met, return False
    return False
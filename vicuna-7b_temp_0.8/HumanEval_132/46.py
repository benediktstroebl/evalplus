
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
    # Define a variable to store the length of the string
    string_length = len(string)

    # Iterate over each character in the string
    for i in range(string_length):
        # Check if the character is a square bracket
        if string[i] == '[':
            # If the previous character is also a square bracket, then check if it is nested
            if i - 1 >= 0 and string[i - 1] == '[':
                # If the previous character is a square bracket, then check if it is nested by checking if
                # the length of the sequence of nested brackets is greater than 2
                nested = True
                for j in range(i - 1, string_length):
                    if string[j] == '[':
                        nested = False
                        break
                    elif string[j] == ']':
                        nested = True
                        break
                # Return True if the sequence of nested brackets is greater than 2
                return nested
            # If the previous character is not a square bracket, then the current character is the start of
            # a nested sequence, so check if the next character is also a square bracket
            else:
                # If the next character is also a square bracket, then the current character is nested
                if string[i] == '[':
                    return True
                # If the next character is not a square bracket, then the current character is not nested
                else:
                    return False
        # If the character is not a square bracket, then check if the next character is a square bracket
        elif string[i] == ']':
            # If the next character is a square bracket, then check if the previous character is a square bracket
            if i + 1 < string_length and string[i + 1] == '[':
                # If the previous character is a square bracket, then check if the current and next characters
                # are nested, and return True if they are
                nested = True
                for j in range(i + 2, string_length):
                    if j == i + 1 and string[j] == '[':
                        nested = False
                    elif j == i


def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Use a variable to hold the current character
    current_char = s[0]
    # Use a for loop to iterate through the string
    for char in s:
        # If the current character is different from the previous character
        if char == ' ':
            # Append the current character to the current word
            current_word += char
        else:
            # Replace the current word with a new word where the characters
            # are arranged in ascending order based on their ASCII values
            current_word = chr(ord(current_char) + ord(char))
        # If the end of the string is reached, add the current word to the result
        if char == '':
            result += current_word
        # Update the current character with the next character
        current_char = char
    # Return the result
    return ' '.join(result)

def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    # This is an array that will contain the words
    words = []
    # Loop through each character in the string
    for i in range(len(s)):
        # If the current character is a space or comma, add the current word to the array
        # and reset the current word to an empty string
        if s[i] == ' ' or s[i] == ',':
            words.append(current_word)
            current_word = ''
        # Otherwise, add the current character to the current word
        else:
            current_word += s[i]

    # Add the last word to the array
    words.append(current_word)

    # Return the array of words
    return words


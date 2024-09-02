
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    current_word = ""
    last_word = ""
    last_comma = ""
    for char in s:
        if char == ",":
            if last_word:
                words.append(current_word)
            words.append(last_word)
            current_word = ""
            last_word = ""
            last_comma = ""
        elif char == " ":
            if current_word:
                words.append(current_word)
            current_word = last_word
            last_comma = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

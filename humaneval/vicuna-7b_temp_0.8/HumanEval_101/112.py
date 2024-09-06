
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    comma = False
    last_word = ""
    for char in s:
        if char == " ":
            if comma:
                words.append(last_word)
            comma = False
            last_word = ""
        elif char == ",":
            if comma:
                words.append(last_word)
                comma = False
            else:
                words.append(last_word)
                last_word = ""
            comma = True
        elif comma:
            last_word += char
        else:
            last_word += char
    if comma:
        words.append(last_word)
    return words


def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    last_index = 0
    for i in range(0, len(s)):
        if s[i] == " " or s[i] == ",":
            words.append(s[last_index:i])
            last_index = i + 1
    words.append(s[last_index:])
    return words
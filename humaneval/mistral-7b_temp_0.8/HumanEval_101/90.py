
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    word = ''
    words = []
    for i in range(len(s)):
        if s[i] != ',' and s[i] != ' ':
            word += s[i]
        else:
            words.append(word)
            word = ''
    words.append(word)
    return words


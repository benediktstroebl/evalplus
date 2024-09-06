
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    index = 0
    while index < len(s):
        if s[index] == " ":
            words.append(s[index].strip())
            index += 1
        else:
            words.append(s[index-1].strip())
            index += 1
    return words

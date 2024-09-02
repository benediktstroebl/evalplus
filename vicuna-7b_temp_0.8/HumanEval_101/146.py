
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    for c in s:
        if c == " ":
            words.append(words_string(s[s.find(s)+1:]))
            break
        elif c == ",":
            words.append(words_string(s.split(",")[0]))
            break
    return words

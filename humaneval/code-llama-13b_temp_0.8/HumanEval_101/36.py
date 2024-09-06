
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    if len(s) == 0:
        return []
    
    if s[0] == ' ':
        return words_string(s[1:])
    
    if s[0] == ',':
        return words_string(s[2:])
    
    if s[0] != ' ' and s[0] != ',':
        i = 0
        while s[i] != ' ' and s[i] != ',':
            i += 1
        return [s[:i]] + words_string(s[i:])


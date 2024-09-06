
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # pattern for spliting on whitespace or comma
    pattern = re.compile(r'\s*,\s*|\s+')
    
    # split the string on whitespace or comma
    words = pattern.split(s)
    
    # remove any empty strings
    words = filter(None, words)
    
    # return the words as an array
    return words

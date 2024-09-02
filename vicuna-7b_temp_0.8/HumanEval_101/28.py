
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Remove leading and trailing spaces
    s = s.strip()
    # Split by commas or spaces
    words = s.split()
    # Remove any remaining leading or trailing spaces
    words = [word.strip() for word in words]
    return words

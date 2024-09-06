
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Define a helper function to split the string by commas or spaces
    def split_string(s, sep=" "):
        """
        Split the string s by the separator sep and return a list of the words.
        
        >>> split_string("hello, world", ",")
        ['hello', 'world']
        >>> split_string("hello, world", ",")
        ['hello', 'world']
        """
        return [word.strip() for word in s.split(sep)]
    
    # Use the helper function to split the string and return the array of words
    return split_string(s)

def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string using commas and spaces as delimiters
    words = s.split(", ")
    words = [word for sublist in [word.split() for word in words] for word in sublist]
    
    return words


def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    # Generate a list by splitting s on commas and/or spaces
    s_list = s.split(",")
    s_list = s_list + s.split(" ")
    # Remove empty strings
    s_list = [x for x in s_list if x]
    return s_list


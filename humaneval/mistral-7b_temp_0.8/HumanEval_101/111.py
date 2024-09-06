
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Solution goes here
    word_list = []
    for element in s:
        if element == " " or element == ",":
            continue
        word_list.append(element)
    return word_list
    # return s.split(",")



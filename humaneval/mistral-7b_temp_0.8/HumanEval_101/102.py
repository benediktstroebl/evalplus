
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    return s.split()

    # Here we split the string into words by using the split() method.
    # Then we return the array of words.

    # Note that this solution is not optimized, as we are creating a new array
    # of words for every string. A more efficient solution would be to use a
    # list comprehension to create the array of words once and return it.

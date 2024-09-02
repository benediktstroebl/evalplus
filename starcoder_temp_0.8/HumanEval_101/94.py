
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    #split the string by commas
    split_string = s.split(",")
    #split the string by spaces
    for i in range(len(split_string)):
        if'' in split_string[i]:
            split_string[i] = split_string[i].split()
    #join all the arrays
    split_string = [x for i in split_string for x in i]
    #remove the spaces
    split_string = [i.strip() for i in split_string]
    #return array
    return split_string

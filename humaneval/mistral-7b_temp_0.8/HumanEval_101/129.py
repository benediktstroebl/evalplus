
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    str_list = []

    for char in s:
        if char.isspace():
            str_list.append(char)

    for i in range(len(str_list)):
        str_list[i] = str_list[i].strip()

    print(str_list)



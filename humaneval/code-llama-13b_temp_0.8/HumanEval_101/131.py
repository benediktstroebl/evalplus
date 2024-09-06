
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # your code here
    s_list = s.split(',')
    new_s_list = []
    for i in s_list:
        i_list = i.split()
        for j in i_list:
            new_s_list.append(j)
    
    return new_s_list

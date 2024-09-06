
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    a = []
    for i in range(len(s)):
        if s[i] == " " or s[i] == ", ":
            if a != []:
                a.append(s[i - 1])
            a.append(s[i])

    if a[len(a) - 1] == " ":
        a.pop()

    return a

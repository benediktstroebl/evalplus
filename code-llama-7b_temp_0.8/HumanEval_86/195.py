
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    if s == "":
        return s
    else:
        list_string = s.split()
        index = 0
        for index in range(len(list_string)):
            new_word = ""
            word = list_string[index]
            for c in word:
                new_word += chr(ord(c))
            list_string[index] = new_word
        new_s = ""
        for word in list_string:
            new_s += word + " "
        return new_s


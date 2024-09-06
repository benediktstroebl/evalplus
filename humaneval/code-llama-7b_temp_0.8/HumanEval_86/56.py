
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
    # create a new string with no spaces or punctuation
    temp_str = s.replace(' ', '')
    temp_str = temp_str.replace('!', '')
    temp_str = temp_str.replace('?', '')
    temp_str = temp_str.replace('!', '')
    temp_str = temp_str.replace(',', '')
    temp_str = temp_str.replace('.', '')
    temp_str = temp_str.replace('?', '')
    temp_str = temp_str.replace(';', '')
    temp_str = temp_str.replace(':', '')
    temp_str = temp_str.replace('-', '')
    temp_str = temp_str.replace('_', '')
    temp_str = temp_str.replace('"', '')
    temp_str = temp_str.replace("'", '')
    temp_str = temp_str.replace("(", "")
    temp_str = temp_str.replace(")", "")
    temp_str = temp_str.replace("/", "")
    temp_str = temp_str.replace("\\", "")
    temp_str = temp_str.replace("[", "")
    temp_str = temp_str.replace("]", "")
    temp_str = temp_str.replace("{", "")
    temp_str = temp_str.replace("}", "")
    temp_str = temp_str.replace("*", "")
    temp_str = temp_str.replace("&", "")
    temp_str = temp_str.replace("`", "")
    temp_str = temp_str.replace("~", "")
    temp_str = temp_str.replace("$", "")
    temp_str = temp_str.replace("^", "")
    temp_str = temp_str.replace("#", "")
    temp_str = temp_str.replace("@", "")
    temp_str = temp_str.replace("|", "")
    temp_str = temp_str.replace("0", "")
    temp_str = temp_str.replace("1", "")
    temp_str = temp_str.replace("2", "")
    temp_str = temp_str.replace("3", "")

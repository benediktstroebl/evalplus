
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
        return ""
    anti_shuffle_string = ""
    word_list = s.split()

    # check for the space in the string and do anti-shuffle operation on that word
    for word in word_list:
        if word.strip() == "":
            anti_shuffle_string += " "
            continue
        asc_sorted_word = sorted(word)
        asc_sorted_word = "".join(asc_sorted_word)
        anti_shuffle_string += asc_sorted_word + " "

    return anti_shuffle_string


    anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    anti_shuffle("ehllo") == "ehllo"

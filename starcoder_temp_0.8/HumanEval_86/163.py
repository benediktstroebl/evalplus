
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

    # Use a list of words from the string s
    words = s.split(" ")

    # Use a list for new words
    new_words = []

    for word in words:
        # Use a list for each word
        new_word = []
        for char in word:
            # Use a list for each character
            new_word.append(char)

        # Use string join to merge list to a string
        new_word = "".join(sorted(new_word))
        new_words.append(new_word)

    # Use string join to merge list to a string
    new_s = " ".join(new_words)

    return new_s

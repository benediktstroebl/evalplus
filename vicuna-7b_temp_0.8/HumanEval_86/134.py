
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
    # Use string slicing to split the string into words
    words = s.split()

    # Shuffle the characters in each word
    shuffled_words = []
    for word in words:
        shuffled_word = ""
        for c in word:
            shuffled_word += chr(ord(c) + 1)
        shuffled_words.append(shuffled_word)

    # Join the shuffled words back into a string
    return " ".join(shuffled_words)

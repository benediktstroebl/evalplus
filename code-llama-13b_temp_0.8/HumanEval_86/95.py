
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
    # break the sentence into a list of words
    words = s.split()
    # sort each word
    new_words = []
    for word in words:
        new_word = sorted(word)
        # join the sorted word into string and append to new_words
        new_words.append(''.join(new_word))
    # join the new_words with blank space and return
    return ' '.join(new_words)


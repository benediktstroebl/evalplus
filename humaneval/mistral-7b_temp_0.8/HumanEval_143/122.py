
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    # solution 1
    # this one is the most obvious and explicit one.
    # you iterate the string to find words with prime length.
    # you append those words to a list and return that list as a string
    # however, this can be simplified by reducing the looping
    # as you are not checking the length of the whole word but only the length of the word's characters
    # so you can iterate the string by the length of the word
    # and check if the length is a prime number, then append the word to the list and continue.
    # the words are stored in a list in order so when we return the list, it is the same order as the original sentence
    # the for loop is a nested one.
    # it iterates the whole string and then iterates the string inside the for loop to check if the string length is a prime number
    # at the end of the loop, if the string's length is a prime number, we append the string to the words list
    # and continue the loop
    words = []
    for word in sentence.split(' '):
        if all(i % j

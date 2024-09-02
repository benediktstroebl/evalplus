
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
    # create a list of words
    words = sentence.split()

    # create an empty list to store prime words
    prime_words = []

    # loop through the words
    for word in words:
        # check if the word's length is a prime number
        if is_prime(len(word)):
            # if it is, append the word to the prime_words list
            prime_words.append(word)

    # join the prime words into a string
    new_sentence = " ".join(prime_words)

    # return the new sentence
    return new_sentence


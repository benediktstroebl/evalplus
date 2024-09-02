
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
    # the list of words in the sentence
    words = sentence.split()

    # the list of words whose length is prime
    primes = []

    # loop through the words
    for word in words:
        # check if the length of the word is prime
        if is_prime(len(word)):
            primes.append(word)

    # return the string of words whose length is prime
    return ' '.join(primes)

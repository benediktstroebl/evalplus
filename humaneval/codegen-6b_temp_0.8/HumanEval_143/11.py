
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
    words = ""

    for word in sentence.split():
        if len(word) == 1:
            # one word, we only need to check for primes
            continue

        if not is_prime(len(word)):
            # we need more than one prime number
            raise ValueError("Length of the word {0} is not a prime number".format(word))

        words += word

    return words


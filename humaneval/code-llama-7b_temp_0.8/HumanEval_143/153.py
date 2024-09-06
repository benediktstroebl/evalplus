
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
    # Can we convert the sentence to a list of words?
    # Can we find the length of the words?
    # Can we make a list of prime numbers the same size as the number of words?
    # Can we zip() these two lists together?
    words = sentence.split(" ")
    primes = []
    for word in words:
        if is_prime(len(word)):
            primes.append(word)
    return " ".join(primes)

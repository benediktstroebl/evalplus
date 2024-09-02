
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
    # make sure the string is lowercase
    sentence = sentence.lower()

    # get a list of the words in the sentence
    words = sentence.split()

    # get a list of the primes
    primes = [num for num in range(2, 101) if is_prime(num)]

    # the words that are in the sentence and are prime
    primes_words = [word for word in words if len(word) in primes]

    # return a single string with all of the words in the correct order
    return " ".join(primes_words)

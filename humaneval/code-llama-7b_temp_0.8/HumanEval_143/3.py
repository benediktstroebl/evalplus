
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
    #################
    # MEMORY LIMIT #
    #################
    # Runtime: 112 ms, faster than 87.55% of Python3
    # Memory Usage: 14.9 MB, less than 35.16% of Python3
    words = sentence.split()

    def is_prime(n):
        return not (n == 1 or n == 2 or n == 3 or n == 5 or n == 7)

    return " ".join(filter(is_prime, map(len, words)))


    #################
    # MEMORY ERROR #
    #################
    # Time Limit Exceeded
    # words = sentence.split()
    # return " ".join(filter(lambda x: not (x == 1 or x == 2 or x == 3 or x == 5 or x == 7), map(len, words)))


    #################
    # ACCORDING TO #
    #################
    # Runtime: 68 ms, faster than 97.35% of Python3
    # Memory Usage: 14.8 MB, less than 35.16% of Python3
    def is_prime(n):
        return n > 1 and all(n % i for i in range(2, n))

    return " ".join(filter(is_prime, map(len, sentence.split())))


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
    #############
    # Solution 1 #
    #############
    # def words_in_sentence(sentence):
    #     # O(n * log(n))
    #     primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    #     words = sentence.split()
    #     result = []
    #     for word in words:
    #         if len(word) in primes:
    #             result.append(word)
    #     return " ".join(result)

    #############
    # Solution 2 #
    #############
    # def words_in_sentence(sentence):
    #     # O(n)
    #     result = []
    #     for word in sentence.split():
    #         if is_prime(len(word)):
    #             result.append(word)
    #     return " ".join(result)

    #############
    # Solution 3 #
    #############
    # import math
    # def words_in_sentence(sentence):
    #     # O(n)
    #     result = []
    #     for word in sentence.split():
    #         if is_prime(len(word)):
    #             result.append(word)
    #     return " ".join(result)

    #############
    # Solution 4 #
    #############
    # def words_in_sentence(sentence):
    #     # O(n * log(log(n)))
    #     result = []
    #     for word in sentence.split():
    #         if is_prime(len(word)):
    #             result.append(word)
    #     return " ".join(result)

    #############
    # Solution 5 #
    #############
    # def words_in_sentence(sentence):
    #    

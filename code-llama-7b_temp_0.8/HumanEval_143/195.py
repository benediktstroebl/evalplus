
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
    # MEMORY:
    # length = 40MB
    #
    # SOLUTION 1:
    # runtime 22.98%
    #################
    import math

    def is_prime(num):
        if num % 2 == 0 and num > 2:
            return False
        return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

    words = sentence.split(" ")
    words_list = []

    for word in words:
        if is_prime(len(word)):
            words_list.append(word)

    return " ".join(words_list)

    #################
    # SOLUTION 2:
    # runtime 65.97%
    #################
    # from functools import reduce
    #
    # def is_prime(num):
    #     if num % 2 == 0 and num > 2:
    #         return False
    #     return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))
    #
    # words = sentence.split(" ")
    # words_list = []
    #
    # for word in words:
    #     if is_prime(len(word)):
    #         words_list.append(word)
    #
    # return reduce(lambda x, y: x + " " + y, words_list)

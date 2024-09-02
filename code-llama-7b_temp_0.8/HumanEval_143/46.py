
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
    # def is_prime(num):
    #     if num == 1:
    #         return False
    #     for i in range(2, num):
    #         if num % i == 0:
    #             return False
    #     return True

    # def is_prime(num):
    #     return num == 2 or num == 3 or num == 5 or num == 7

    # [len(word) for word in sentence.split() if is_prime(len(word))]
    # print([len(word) for word in sentence.split() if is_prime(len(word))])

    # from math import sqrt
    # def is_prime(num):
    #     for i in range(2, int(sqrt(num)) + 1):
    #         if num % i == 0:
    #             return False
    #     return True

    # res = [word for word in sentence.split() if is_prime(len(word))]
    # return " ".join(res)

    # import math
    # res = [word for word in sentence.split() if is_prime(len(word))]
    # return " ".join(res)

    # import math
    # res = [word for word in sentence.split() if is_prime(len(word))]
    # return " ".join(res)
    # # Faster
    import math
    res = [word for word in sentence.split() if len(word) > 1 and is_prime(len(word))]
    return " ".join(res)


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
    # # Version 1: slow, but understandable: O(n) time, O(1) space
    # words = sentence.split()
    # is_prime = lambda x: (
    #     all(x % i for i in range(2, int(x ** 0.5) + 1)) and x != 1
    # )
    # result = []
    # for word in words:
    #     if is_prime(len(word)):
    #         result.append(word)
    # return " ".join(result)

    # # Version 2: O(n) time, O(1) space
    # words = sentence.split()
    # is_prime = lambda x: (
    #     all(x % i for i in range(2, int(x ** 0.5) + 1)) and x != 1
    # )
    # for idx, word in enumerate(words):
    #     if is_prime(len(word)):
    #         words[idx] = word
    #     else:
    #         words[idx] = ""
    # return " ".join(words)

    # Version 3: O(n) time, O(1) space
    return " ".join(
        word for word in sentence.split() if is_prime(len(word))
    )

